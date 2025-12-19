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

# Naplózás beállítása 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Adatbázis táblák létrehozása
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title=API_TITLE)

# Dependency az adatbázis kapcsolathoz
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Végpont: Lista 
@app.get("/products", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    logger.info("Termékek listázása...")
    return db.query(models.Product).all()

# 2. Végpont: Részletek (ID alapján) 
@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Termék nem található")
    return product

# 3. Végpont: Statisztika [cite: 19, 27]
@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    if not products: 
        return {"avg_price": 0, "count": 0}
    
    # Funkcionális elem: sum() és generátorkifejezés használata [cite: 17, 34]
    avg = sum(p.price for p in products) / len(products)
    return {"avg_price": round(avg, 2), "count": len(products)}

# Automatikus háttérfolyamat / Adat API lánc [cite: 12, 21, 24]
@app.post("/auto-update")
async def background_update(db: Session = Depends(get_db)):
    """
    Aszinkron feladat, amely szimulál egy külső adatforrásból való frissítést.
    """
    logger.info("Automatizált adatfrissítés indítása...")
    # Itt lehetne egy BeautifulSoup scraping vagy egy külső API hívás requests-szel [cite: 24]
    await asyncio.sleep(1) # Aszinkron várakozás szimulálása [cite: 6]
    
    # Példa: Procedurális elem egy új rekord beszúrására [cite: 17]
    new_item = models.Product(name="Automatizált Termék", price=99.9)
    db.add(new_item)
    db.commit()
    
    return {"status": "success", "message": "Adatok frissítve külső forrásból"}

# Új termék manuális felvétele
@app.post("/products", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductBase, db: Session = Depends(get_db)):
    db_product = models.Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        logger.error(f"Sikertelen törlés: ID {product_id} nem található") [cite: 25]
        raise HTTPException(status_code=404, detail="Termék nem található")
    
    db.delete(product)
    db.commit()
    logger.info(f"Termék törölve: ID {product_id}") [cite: 25]
    return {"message": "Termék sikeresen törölve"}