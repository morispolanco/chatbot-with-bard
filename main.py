import streamlit as st
import requests

def get_bard_answer(prompt):
    url = "https://api.bard.ai/v1/query"
    params = {
        "query": prompt,
        "language": "es",
        "model": "PaLM2"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("result", {}).get("content", "No answer")
    except requests.exceptions.RequestException as e:
        st.error(f"Error al obtener respuesta de Bard: {e}")
        return "Error"

def main():
    st.title("Chatbot con Bard")
    st.caption("Powered by BARD")

    if "qa_history" not in st.session_state:
        st.session_state.qa_history = []

    user_question = st.text_input("¿Cuál es tu pregunta?")

    if st.button("Obtener respuesta"):
        bot_answer = get_bard_answer(user_question)
        st.session_state.qa_history.append({"question": user_question, "answer": bot_answer})

    for entry in st.session_state.qa_history:
        st.text(f"Pregunta: {entry['question']}")
        st.text(f"Respuesta: {entry['answer']}")
        st.markdown("---")

if __name__ == "__main__":
    main()
