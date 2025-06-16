import streamlit as st

# entrada de texto
entrada_texto = st.text_input("Inserte texto: ")
st.write("Texto del text_input: ", entrada_texto)

# entrada de números
entrada_numero = st.number_input("Inserte un número: ")
st.write("Número del number_input: ", entrada_numero)