import streamlit as st

def suma(a, b):
    return a + b

if st.button("suma"):
    resultado = suma(5, 10)
    st.write("El resultado de los números es: ", resultado)