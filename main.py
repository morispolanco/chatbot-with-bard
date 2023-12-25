import streamlit as st
from streamlit_chat import st_chatbot
import requests

def search_product_price(product_name):
    # Configura la URL de la API de Bard para buscar el precio del producto en Guatemala
    api_url = "https://api.bard.co/v1/products"
    params = {
        "country": "GT",  # Guatemala
        "product": product_name,
    }

    # Realiza la solicitud a la API
    response = requests.get(api_url, params=params)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        data = response.json()
        # Verifica si se encontraron resultados
        if data.get("results"):
            # Devuelve el precio más bajo encontrado
            return data["results"][0]["price"]
        else:
            return "No se encontraron resultados para el producto en Guatemala."
    else:
        return "Error al buscar el precio del producto."

def main():
    st.title("Búsqueda de Precio Más Bajo en Guatemala")
    
    # Crea el chatbot de Streamlit
    chatbot = st_chatbot()

    # Escucha los mensajes del chatbot
    user_message = st.text_input("Ingrese el nombre del producto:")
    
    if user_message:
        # Muestra el mensaje del usuario en el chat
        chatbot.user_msg(user_message)

        # Busca el precio del producto y muestra la respuesta en el chat
        bot_response = search_product_price(user_message)
        chatbot.bot_msg(bot_response)

if __name__ == "__main__":
    main()
