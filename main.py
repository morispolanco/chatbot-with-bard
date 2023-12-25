import streamlit as st
from streamlit_chat import message
from requests import get

# Función para obtener el precio más bajo de un producto en Guatemala
def get_lowest_price(product_name):
    url = "https://api.bard.ai/v1/query"
    params = {
        "query": f"precio mas bajo en guatemala de un {product_name}",
        "language": "es",
        "model": "PaLM2"
    }
    response = get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["result"]["price"]
    else:
        return None

# Function to process incoming messages
def handle_incoming_message(message):
    product_name = message.text
    if product_name:
        price = get_lowest_price(product_name)
        if price is not None:
            message.reply(f"El precio más bajo de {product_name} en Guatemala es de Q{price}")
        else:
            message.reply(f"No se pudo encontrar el precio de {product_name}")

# Register the message handler
message.on_message(handle_incoming_message)

# Create the chat interface
chat = message()
