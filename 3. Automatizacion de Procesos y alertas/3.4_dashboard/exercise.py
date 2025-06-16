import streamlit as st
import yfinance as yf
import plotly.express as px

# wide mode: modo apaisado:
st.set_page_config(layout="wide")

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
# Mostrar en formato dataframe
st.dataframe(data)

columns = tuple(data.columns)

# radio 
radio = st.radio("Selecciona una columna: ",
                 columns)
data_col = data[[radio]]
st.write(data_col)

# Visualización usando plotly:
data = data.rename_axis('Date').reset_index()
fig = px.line(data, x = data["Date"], y = data[radio], title = f"Cotización de {radio}")
st.plotly_chart(fig, use_container_width=True)