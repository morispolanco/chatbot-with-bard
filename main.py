from bardapi import Bard
import streamlit as st
from streamlit_chat import message

st.title("KHAI")
st.subheader("Power by BARD")
st.caption("Author: Davann Tet")
st.caption("KHAI")

# Configurar la clave de la API de Bard
os.environ['_BARD_API_KEY'] = "bAjcVAWV5diEbSb5Mmhk7u1wV06cKjVc5LMCLyWt4xPnIJTMDrULSF__pa-hcgFusHzTpQ."

def get_bard_answer(prompt):
    return Bard().get_answer(prompt)['content']

def main():
    if 'qa_history' not in st.session_state:
        st.session_state['qa_history'] = []

    user_question = st.text_input("What is your question?")

    if user_question:
        bot_answer = get_bard_answer(user_question)
        st.session_state['qa_history'].insert(0, {'question': user_question, 'answer': bot_answer})

    if st.session_state['qa_history']:
        for idx, entry in enumerate(st.session_state['qa_history']):
            message(entry['question'], key=f"{idx}user", is_user=True)
            message(entry['answer'], key=f"{idx}bot", is_user=False)

if __name__ == "__main__":
    main()
