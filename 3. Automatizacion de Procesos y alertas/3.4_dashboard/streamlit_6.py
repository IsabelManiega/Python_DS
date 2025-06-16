import streamlit as st

# multiselect: opcion multiple
opciones = st.multiselect("Tus Frameworks favoritos de Python son:", 
                          ["Dask", "Spark", "Vaex", "Streamlit"])

st.write("Has elegido los siguientes frameworks: ", opciones)