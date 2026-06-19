from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear

app = FastAPI()

lista_clientes:list[Cliente] = []



@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return lista_clientes

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def listar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente

@app.post("/clientes", response_model=Cliente)
def crear_cliente(datos_cliente: ClienteCrear):
    Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    lista_clientes.append(Cliente_val)
    return Cliente_val