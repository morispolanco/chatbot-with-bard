from bardapi import Bard
import os
import streamlit as st
from streamlit_chat import message

# Cargar la configuración desde un archivo JSON
with open('config.json') as config_file:
    data = json.load(config_file)

# Obtener la clave de la API de Bard desde la configuración
bard_api_key = os.getenv("BARD_API_KEY")

# Inicializar la API de Bard
bard = Bard(token=bard_api_key, timeout=30)

# Verificar si 'answer.json' existe y crearlo si no
if not os.path.exists("answer.json"):
    with open("answer.json", "w") as f:
        f.write("")  # Puedes escribir algo inicial si lo deseas

# Función para obtener la respuesta del chatbot
def get_bard_answer(prompt):
    try:
        return bard.get_answer(prompt)['content']
    except Exception as e:
        st.error(f"Error al obtener respuesta de Bard: {e}")
        return None

# Función principal para ejecutar la aplicación
def main():
    st.title("Bard Chatbot")

    # Resto del código...

    # Botón para enviar la pregunta al chatbot
    if st.button("Enviar Pregunta"):
        user_question = st.text_input("Pregunta al Chatbot:")
        if user_question:
            bot_answer = get_bard_answer(user_question)
            if bot_answer is not None:
                st.success(f"Respuesta del Chatbot: {bot_answer}")
            else:
                st.error("No se pudo obtener una respuesta del Chatbot")

if __name__ == "__main__":
    main()
