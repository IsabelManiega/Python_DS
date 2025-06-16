import streamlit as st

# selectbox: seleccionar una opción
opcion = st.selectbox("Tu lenguaje de programación favorito",
                      ("Python", "C++", "Matlab"))

st.write("Seleccionaste: ", opcion)