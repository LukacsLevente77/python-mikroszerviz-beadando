import streamlit as st
import requests
import pandas as pd

st.title("Mikroszerviz Frontend")

BACKEND_URL = "https://python-mikroszerviz-beadando.onrender.com" # Render-en majd a Render URL-re kell írni [cite: 31]

st.header("Új termék hozzáadása")
name = st.text_input("Termék neve")
price = st.number_input("Ár", min_value=0.0)

if st.button("Mentés"):
    res = requests.post(f"{BACKEND_URL}/products", json={"name": name, "price": price})
    if res.status_code == 200:
        st.success("Sikeres mentés!")

st.header("Statisztika és Vizualizáció")
if st.button("Adatok frissítése"):
    stats = requests.get(f"{BACKEND_URL}/stats").json()
    products = requests.get(f"{BACKEND_URL}/products").json()
    
    st.write(f"Összes termék: {stats['count']}")
    st.write(f"Átlagos ár: {stats['avg_price']}")
    
    if products:
        df = pd.DataFrame(products)
        st.bar_chart(df.set_index("name")["price"]) # Vizualizáció [cite: 27]