import streamlit as st
import quandl

# titulo
st.title("Gráfica con Streamlit para Finanzas")

# Netflix (NFLX), Tesla (TSLA)
empresas = ("GOOGL", "AAPL", "TSLA", "MSFT", "NFLX")

# Selecciona una empresa de ellas:
opcion = st.selectbox("Selecciona una de estas empresas:",
                      empresas)
st.write("Has elegido: ", opcion)

# 1 año a 5 de 1 en 1 para este ejemplo:
anho = st.slider("Número de años que quieres plotear:",
                 1, 5, 1)
st.write("Has elegido: ", anho, " años")

anho_final = 2015 + anho
st.write("año final: ", anho_final)

# Obtención de datos via quandl:
data = quandl.get(f"WIKI/{opcion}",
                  start_date="2015-1-1",
                  end_date=f"{anho_final}-12-31")

# head()
st.write("Vamos a imprimir los primeros 5 valores del dataset")
st.write(data.head())

# tail()
st.write("Vamos a imprimir los últimos 5 valores del dataset")
st.write(data.tail())

# elegimos la cotización de cierre
st.write("Vamos a seleccionar sólamente la columna de close")
data = data[["Close"]]
st.write(data)

# Ploteamos gráfica
st.write("Vamos a plotear el gráfico seleccionado")
st.write("Gráfico seleccionado: ", opcion)
st.write("Año inicial: 2015, año final: ", anho_final)
st.line_chart(data)