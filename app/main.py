from fastapi import FastAPI, HTTPException, status
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar


app = FastAPI()

lista_clientes:list[Cliente] = []
lista_facturas:list[Factura] = []
lista_transacciones:list[Transaccion] = []



@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes



@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
    raise HTTPException(
        status_code=400, detail=f"El cliente con id{cliente_id}, no esxiste,"
    )


@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    id_cliente = len(lista_clientes) + 1
    Cliente_val.id = id_cliente
    lista_clientes.append(Cliente_val)
    return Cliente_val


@app.patch("/clientes{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            Cliente_val.id = cliente_id
            lista_clientes[i] =  Cliente_val
            return Cliente_val
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )


@app.delete("/clientes{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            Cliente_eliminado = lista_clientes.pop(i)
            return Cliente_eliminado
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )


#Crear los endpoint para facturas

    
@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas


@app.get("/facturas{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factra con id {factura_id}, no esxiste,"
    )



@app.post("/facturas{cliente_id}", response_model=Factura)
async def Crear_factura(cliente_id: int, datos_factura: FacturaCrear):
    cliente_encontrado = None
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente

    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe."
        )
    
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.cliente = cliente_encontrado

    factura_val.id = len(lista_facturas) + 1
    lista_facturas.append(factura_val)
    return factura_val

    

@app.patch("/facturas{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass


@app.delete("/facturas{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura):
    pass


#Crear endpoint para transacciones

@app.get("/transacciones", response_model=list[Transaccion])
async def listar_Transacciones():
    return lista_transacciones


@app.get("/transacciones{id_transacciones}", response_model=list[Transaccion])
async def listar_Transaccion(id_transaccion: int):
    pass


@app.post("/transacciones{factura_id}", response_model=Transaccion)
async def crear_Transaccion(factura_id: int, datos_transaccion: TransaccionCrear):
     factura_encontrada = None
     for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura

     if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe."
        )
    
     transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
     transaccion_val.factura_id = factura_id
     factura_encontrada.transacciones.append(transaccion_val)

     transaccion_val.id = len(lista_transacciones)+1
     
     lista_transacciones.append(transaccion_val)
     return transaccion_val


@app.patch("/transacciones{id_transacciones}", response_model=Transaccion)
async def editar_Transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass


@app.delete("/transacciones{id_transacciones}", response_model=Transaccion)
async def eliminar_Transaccion(id_transaccion: int):
    pass