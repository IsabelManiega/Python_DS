import streamlit as st
import yfinance as yf

st.title("Gráfica con Streamlit para cotizacion en bolsa de varias empresas")

empresas = ("GOOGL", "AAPL", "TSLA", "MSFT", "NFLX")

opcion = st.selectbox("Selecciona una de estas empresas:",
                      empresas)
st.write("Has elegido: ", opcion)

años = st.slider("Numeros de años que quieres mostrar: ",
                 1, 5, 1)
st.write("Has elegido: ", años, ' años')

año_final = 2015 + años
st.write("año final: ", año_final)

data = yf.download(opcion, "2015-1-1",
                  f"{año_final}-12-31")
st.write(data.head())

data_close = data[["Close"]]
st.write(data_close)

st.line_chart(data_close)