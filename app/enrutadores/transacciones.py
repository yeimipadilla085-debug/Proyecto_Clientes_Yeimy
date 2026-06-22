from fastapi import  APIRouter, HTTPException, status
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from modelos.facturas import Factura
from listas import lista_facturas, lista_transacciones

rutas_transacciones = APIRouter()  

#lista_facturas: list[Factura] = []
#lista_transacciones: list[Transaccion] = []

@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_Transacciones():
    return lista_transacciones


@rutas_transacciones.get("/transacciones/{id_transacciones}", response_model=Transaccion)
async def listar_Transaccion(id_transaccion: int):
    for transaccion in lista_transacciones:
        if transaccion.id == id_transaccion:
            return transaccion
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La transaccion con id {id_transaccion}, no existe."
    )


@rutas_transacciones.post("/transacciones{id_transacciones}", response_model=Transaccion)
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


@rutas_transacciones.patch("/transacciones{id_transacciones}", response_model=Transaccion)
async def editar_Transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass


@rutas_transacciones.delete("/transacciones{id_transacciones}", response_model=Transaccion)
async def eliminar_Transaccion(id_transaccion: int):
    pass