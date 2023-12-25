from bardapi import Bard
import os
import streamlit as st
from streamlit_chat import message

st.title("KHAI")
st.subheader("Power by BARD")
st.caption("Author: Davann Tet")
st.caption("KHAI")

os.environ['_BARD_API_KEY'] = "ABTWhQF55IO_Kq_Uc1Knk24BEfyjWjSVyMZ1yuRIL3IKNhpeyBlsjMhTkWrXllgR_gQxQVekQCaW"
def answer(promt):
    answer = Bard().get_answer(str(promt))['content']
    return answer

def question():
    q = st.text_input("What is your question?")
    return q

if 'answer' not in st.session_state:
    # st.session_state['answer'] = []
    with open("answer.json","r") as f:
        ans = f.read().split("$#$@$")[:-1][::-1]
        if ans!=[]:
            st.session_state['answer'] = ans
        else:
            st.session_state['answer'] = []
    
if 'question' not in st.session_state:
    # st.session_state['question']=[]
    with open("question.json","r") as f:
        que = f.read().split("$#$@$")[:-1][::-1]
        if que!=[]:
            st.session_state['question']=que
        else:
            st.session_state['question']=[]
    

input = question()

if input:
    ans = answer(input)
    st.session_state['answer'].insert(0,ans)
    st.session_state['question'].insert(0,input)
    with open("answer.json","+a") as f:
        f.write(str(ans)+"$#$@$")
        f.close()
    with open("question.json","+a") as f:
        f.write(str(input)+"$#$@$")
        f.close()    


if st.session_state['answer']:
    for i in range(len(st.session_state['answer'])):
        message(st.session_state['question'][i],key=str(i)+"user",is_user=True)
        message(st.session_state['answer'][i],key=str(i)+"bot",is_user=False)
