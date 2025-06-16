# Para ejecutar usaremos streamlit run <nombre del script>

import pandas as pd
import streamlit as st

st.write("Primera Aplicación con Streamlit")
st.write("Podemos escribir lo que queramos, texto, en esta ocasión")

st.write("Incluso un DataFrame como a continuación")
df = pd.DataFrame({"a": [10, 30, 20, 40, 20], "b": [40, 10, 20, 50, 60]})

st.write(df)
st.write("Podemos plotear un gráfico de barras")
st.bar_chart(df)