# Mikroszerviz Alapú Termékkezelő Rendszer

## Projekt célja
A rendszer egy Python alapú mikroszerviz-architektúra, amely bemutatja a procedurális, funkcionális és objektumorientált programozási szemléletet.

## Technológiák
- **Backend:** FastAPI (REST API)
- **Frontend:** Streamlit
- **Adatbázis:** SQLite + SQLAlchemy ORM
- **Adatvalidáció:** Pydantic
- **Tesztelés:** Pytest

## Architektúra leírása
A rendszer moduláris felépítésű:
- `backend/`: Tartalmazza az API végpontokat, az adatbázis modelleket és az üzleti logikát.
- `frontend/`: A Streamlit alapú felhasználói felület.
- `tests/`: Automatikus egységtesztek.

## Telepítés és Futtatás
1. Virtuális környezet létrehozása: `python -m venv venv
2. Aktiválás:
   - Windows: `.\venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. Függőségek telepítése: `pip install -r requirements.txt`
4. Indítás:
   - Backend: `uvicorn backend.main:app --reload`
   - Frontend: `streamlit run frontend/app.py`

## Deploy Linkek
- **Backend (Render):** https://python-mikroszerviz-beadando.onrender.com
- **Frontend (Streamlit Cloud):** https://python-mikroszerviz-beadando-nhkjmbkolqkvkzyppkn5f4.streamlit.app/
