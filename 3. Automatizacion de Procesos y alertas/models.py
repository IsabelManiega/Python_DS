# Crearemos el modelo de los datos a aguardar
from pydantic import BaseModel

# Modelo de datos:
class Car(BaseModel):
    #id: int 
    brand: str 
    model: str 
    production_year: int
    convertible: bool