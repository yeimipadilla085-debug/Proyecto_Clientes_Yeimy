from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def saludar():
    return {"mensaje": "Hola"}



clientes = [
    {"id": 1, "nombre": "Carlos Mendoza"},
    {"id": 2, "nombre": "Ana María Restrepo"},
    {"id": 3, "nombre": "Juan Fernando Hoyos"}
]


@app.get("/clientes")
def obtener_clientes():
    return clientes