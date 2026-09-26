import streamlit as st
st.title("My first streamlit App!!!")
st.header("Welcome to my AI application!")
st.subheader("Bindu")
st.markdown("*Chinnu*")
name = st.text_input("Enter your name: ")
if st.button("Submit"):
     st.write("Hello", name)
chat=st.chat_input("Enter your question: ")
st.checkbox("Male")
st.checkbox("Female")
st.number_input("Enter your age")
st.slider("pick a number", 0, 100)