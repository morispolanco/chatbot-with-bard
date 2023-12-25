import streamlit as st
from streamlit_chat import message
import requests

API_URL = "https://api.example.com/price"

st.set_page_config(page_title="Buscador de Precios")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_price(product):
    params = {"product": product, "country": "GT"}
    response = requests.get(API_URL, params=params)
    return response.json()["price"]

def get_text():
    input_text = st.text_input("Tu: ","Hola, busco precio de iPhone 14") 
    return input_text

user_input = get_text()

if user_input:
    product = user_input.split()[-1]  
    price = get_price(product)
    output = f"El precio más bajo del {product} es {price}"
    
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i) + '_bot')
