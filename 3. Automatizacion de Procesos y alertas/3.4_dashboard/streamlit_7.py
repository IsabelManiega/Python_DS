import streamlit as st
from datetime import time

# slider - ejemplo
# Declaramos el texto del slider, el numero de inicio, 
# numero de fin y el paso en el que empieza
lenguajes = st.slider("¿Cuántos framworks conoces de Python?",
                      0, 15, 1)
st.write("Conoces ", lenguajes, " Frameworks de Python")

# slider - ejemplo2
# Declaramos el texto del slider, el numero de inicio, 
# numero de fin y el intervalo a señalar
rango = st.slider("Selecciona un rango de valores",
                  0.0, 100.0, (25.0, 75.0))
st.write("Rango de valores: ", rango)

# slider - ejemplo 3
hora = st.slider("Hora de la reunion:",
                 value=(time(13,30), time(15,30)))
st.write("Tu reunión tendrá lugar en este intervalo de horas:",
         hora)