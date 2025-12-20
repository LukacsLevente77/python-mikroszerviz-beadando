from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
import logging
import os
import asyncio
from dotenv import load_dotenv

# Konfigurációkezelés .env fájlból 
load_dotenv()
API_TITLE = os.getenv("API_TITLE", "Termék Kezelő API")


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title=API_TITLE)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    logger.info("Termékek listázása...")
    return db.query(models.Product).all()


@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Termék nem található")
    return product


@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    if not products: 
        return {"avg_price": 0, "count": 0}
    

    avg = sum(p.price for p in products) / len(products)
    return {"avg_price": round(avg, 2), "count": len(products)}


@app.post("/auto-update")
async def background_update(db: Session = Depends(get_db)):
    """
    Aszinkron feladat, amely szimulál egy külső adatforrásból való frissítést.
    """
    logger.info("Automatizált adatfrissítés indítása...")

    await asyncio.sleep(1)
    

    new_item = models.Product(name="Automatizált Termék", price=99.9)
    db.add(new_item)
    db.commit()
    
    return {"status": "success", "message": "Adatok frissítve külső forrásból"}


@app.post("/products", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductBase, db: Session = Depends(get_db)):
    db_product = models.Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product