import streamlit as st
from compare_sentence import getAnswer, getSimilarity, add_Entry

st.title("M.Y. Note:")

option = st.radio('test', ['get info', 'update info'])
    
if option == 'get info':
    question = st.text_input("Question: ")

    if question:  
        indx = getSimilarity(question)
        response = getAnswer(indx)

        st.header("Answer")
        st.write(response)
elif option == 'update info':
    New_Question = st.text_input('Enter your question here')
    New_Answer = st.text_input('Enter your answer here')
    btn = st.button('add Knowledgebase')
    
    if btn:
        ret = add_Entry(New_Question, New_Answer)
        st.warning(ret)
        
        







