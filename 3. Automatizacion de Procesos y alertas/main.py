from fastapi import FastAPI, status, Response
from models import Car
import sqlite3

# Para ejecutar: fastapi dev main.py

app = FastAPI()

# Creamos un archivo como extensión .db donde se almacenará la información, si no existe se crea:
conexion=sqlite3.connect("cars.db")


@app.get('/')
async def test():
    return "CARS DATABASE"


# Método GET a la url "/cars/"
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.get('/cars/')
async def cars(response:Response):
    try:
        cursor = conexion.execute("SELECT * FROM cars")
        response = []
        for fila in cursor.fetchall():
            data = {'id': fila[0], 'brand': fila[1], 
                    'model': fila[2], 'production_year': fila[3], 
                    'convertible': fila[4]}
            response.append(data)
        return response
    except Exception as e:
        print("Error al cargar el csv %s" % str(e))
        response.status_code = status.HTTP_404_NOT_FOUND
        return "404 NOT FOUND"     

 
# POST de insertar un nuevo dato en el csv, última línea
# Método POST a la url "/insertData/"
@app.post("/cars/", status_code=201)
async def insert(item:Car):
    conexion.execute("INSERT INTO cars(brand, model, production_year, convertible) VALUES (?,?,?,?)",
                     (item.brand, item.model,
                      item.production_year, item.convertible))
    conexion.commit()
    return item


# PUT actualizar la última línea del csv
# Método PUT a la url "/updateData/" + ID a modificar
@app.put("/cars/{item_id}")
async def updateData(item_id: int, item:Car):
    conexion.execute("UPDATE cars SET brand=?, model=?, production_year=?, convertible=? WHERE id=?;", 
                    (item.brand, item.model, item.production_year, 
                    item.convertible, item_id))
    # Para que se realize el cambio añadimos .commit
    conexion.commit()
    return item

# DELETE eliminar la última línea del csv
# Método Delete a la url "/deleteData/" + id
@app.delete("/cars/{item_id}")
async def deleteData(item_id: int):
    conexion.execute("DELETE FROM cars WHERE id=?;", (item_id, ))
    #  Para que se realize el cambio añadimos .commit
    conexion.commit()
    return {"item_id": item_id, "msg": "Eliminado"}