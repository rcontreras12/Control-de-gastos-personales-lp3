import json
import os 

ARCHIVO_DATOS = "datos/gastos.json"

def cargar_datos():
    """carga los datos desde el archivo JSON. si no existe, retorna una lñista vacia."""
    if not os.path.exists("datos"):
        os.makedirs("dato")

    if not os.path.exists(ARCHIVO_DATOS):
        return []

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.losd(archivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    
def guardar_datos(gastos):
    """Guardar la lista de gastos en el archivo JSON permanentemente."""
    if not os.path.exists("datos"):
        os.makedirs("datos")

    with open(ARCHIVO_DATOS, "W", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, indent=4, ensure_ascii=False)