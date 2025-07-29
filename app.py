import streamlit as st
from langchain_community.llms import Ollama

st.title("🤖 Blog Generator using Llama 2")

topic = st.text_input("Enter the Blog Topic")
audience = st.selectbox("Target Audience", ["General" , "Students" , "Professionals" , "Researchers" , "Others"])
word_count = st.number_input("Number of words", value=100, min_value=50, max_value=500, step=50)

if st.button("Generate Blog"):
    llm = Ollama(model="llama2:7b")
    prompt = f"Write a {word_count}-word blog for {audience} about '{topic}'."
    with st.spinner("Generating blog..."):
        result = llm(prompt)
    st.write(result)
