import streamlit as st

# radio button
radio = st.radio(("Tener en cuenta los Outliers:"), 
                 ("Si", "No"))

if radio == "Si":
    st.write("Eliminaremos los Outliers del dataset")
else:
    st.write("No eliminaremos los Outliers del dataset")
