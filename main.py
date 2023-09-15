from bardapi import Bard
import os
import streamlit as st
from streamlit_chat import message

st.title("KHAI Power by BARD")

os.environ['_BARD_API_KEY'] = "bAjcVOUE3cfwG_GD-4CfKygiiRokhsEAh-L9SUqfA3UYtYMGvI8bcOmdMy94BsZ-H4m5oA."
def answer(promt):
    answer = Bard().get_answer(str(promt))['content']
    return answer

def question():
    q = st.text_input("What is your question?")
    return q

if 'answer' not in st.session_state:
    st.session_state['answer'] = []
if 'question' not in st.session_state:
    st.session_state['question']=[]

input = question()

if input:
    ans = answer(input)
    st.session_state['answer'].append(ans)
    st.session_state['question'].append(input)

if st.session_state['answer']:
    for i in range(len(st.session_state['answer'])):
        message(st.session_state['question'][i],key=str(i)+"user",is_user=True)
        message(st.session_state['answer'][i],key=str(i)+"bot",is_user=False)
