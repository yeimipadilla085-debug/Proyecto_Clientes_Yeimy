# Proyecto: YeimyPadilla pro clientes

## Datos Personales
* **Nombre:** Yeimy Alejandra Padilla Gutierrez
* **Programa:**  Analisis y desarrollo de Software / 3407180
* **Fecha:** Mayo 26 2026

---

## Descripción del Proyecto
Este es un proyecto backend desarrollado con **FastAPI** (Python) que gestiona una API básica para el manejo de clientes. Cuenta con un diseñado para listar clientes.

## Paso a Paso de la Ejecución (Comandos)

Sigue estos pasos en su  terminal para configurar y ejecutar el proyecto desde cero:

### 1. Crear una carpeta (directorio) del proyecto y entrar en él bash o powersell
nombre_pro_clientes

# en caso de que no pueda escribir en la terminal:
cd nombre_pro_clientes

# 2. Activar el entorno:
en la terminal escribir:
1. python -m venv venv
te aparecera una carpeta llamada "venv"

# si en la carpeta "venv" y te dirijes en el apartado de "scripts" y no aparece "activate" volver a ejecutar el mismo codigo

# 3. Activar el entorno:
en la terminal escribir:
1. /venv/Scripts/activate
# 4. instalar Flask
en la terminal escribir:
1. pip install "fastapi[standard]"
2. pip list
# 5. luego de instalar el "flask" y de ver las listas ejecutar lo siguiente. 
antes de ejecutar crea un archivo llamado "main.py" en el cual escribiras el siguiente codigo:

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def saludar():
    return {"mensaje": "Hola"}


ahora ya puedes escrbir en la terminal:
1. fastapi dev main.py
**te devera aparecer unos links. picale al de una url/doc devera entrar a una pagina **
# 6. probar en el navegador:
# Lista de clientes estructurada de forma simple
clientes = [
    {"id": 1, "nombre": "Carlos Mendoza"},
    {"id": 2, "nombre": "Ana María Restrepo"},
    {"id": 3, "nombre": "Juan Fernando Hoyos"}
]

# Endpoint "/clientes" que retorna la lista
@app.route("/clientes")
def obtener_clientes():
    return clientes


### puntos importantes  para tener en cuenta:
venv: es un entorno virtual 
raiz: es la carpeta
servidor: unicon

ctrl + c: apagar el servidor 