import streamlit as st
st.title('hello')
num1=st.number_input('digite o primeiro número:')
num2=st.number_input('digite o segundo número:')

if st.button('soma'):

    resultado=num1+num2

    st.text('resultado:')
    st.title('resultado')
