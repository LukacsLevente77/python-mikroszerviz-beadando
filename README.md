# Mikroszerviz Alapú Termékkezelő Rendszer

## Projekt célja
[cite_start]A rendszer egy Python alapú mikroszerviz-architektúra, amely bemutatja a procedurális, funkcionális és objektumorientált programozási szemléletet[cite: 5, 6].

## Technológiák
- [cite_start]**Backend:** FastAPI (REST API) [cite: 9]
- [cite_start]**Frontend:** Streamlit [cite: 10]
- [cite_start]**Adatbázis:** SQLite + SQLAlchemy ORM [cite: 11, 20]
- [cite_start]**Adatvalidáció:** Pydantic [cite: 20]
- [cite_start]**Tesztelés:** Pytest [cite: 26]

## Architektúra leírása
[cite_start]A rendszer moduláris felépítésű[cite: 16]:
- `backend/`: Tartalmazza az API végpontokat, az adatbázis modelleket és az üzleti logikát.
- `frontend/`: A Streamlit alapú felhasználói felület.
- `tests/`: Automatikus egységtesztek.

## Telepítés és Futtatás
1. [cite_start]Virtuális környezet létrehozása: `python -m venv venv` [cite: 14]
2. Aktiválás:
   - Windows: `.\venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. [cite_start]Függőségek telepítése: `pip install -r requirements.txt` [cite: 41]
4. Indítás:
   - [cite_start]Backend: `uvicorn backend.main:app --reload` [cite: 15]
   - [cite_start]Frontend: `streamlit run frontend/app.py` [cite: 15]

## Deploy Linkek
- [cite_start]**Backend (Render):** [IDE ILLESZD A RENDER LINKET] [cite: 31, 44]
- [cite_start]**Frontend (Streamlit Cloud):** [IDE ILLESZD A STREAMLIT LINKET] [cite: 31, 44]