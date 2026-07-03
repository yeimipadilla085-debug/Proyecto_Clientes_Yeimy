from fastapi import  APIRouter, HTTPException, status
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from modelos.facturas import Factura
from listas import lista_facturas, lista_transacciones
from conexion_bd import Session_dependencia
from sqlmodel import select

rutas_transacciones = APIRouter()  

#lista_facturas: list[Factura] = []
#lista_transacciones: list[Transaccion] = []

@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_Transacciones(sesion: Session_dependencia):
    #consulta = select(Transaccion)
    #lista_transacciones = sesion.exec(consulta).all()
    #return lista_transacciones
    return sesion.exec(select(Transaccion)).all()


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
async def crear_Transaccion(factura_id: int, datos_transaccion: TransaccionCrear, sesion: Session_dependencia):
     
     factura_encontrada = sesion.get(Factura, factura_id)
     if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe."
        )
    
     transaccion_dict = datos_transaccion.model_dump()
     transaccion_dict["factura_id"] = factura_id
     transaccion_val = Transaccion.model_validate(transaccion_dict)

     sesion.add(transaccion_val)
     sesion.commit()
     sesion.refresh(transaccion_val)
     return transaccion_val


@rutas_transacciones.patch("/transacciones{id_transacciones}", response_model=Transaccion)
async def editar_Transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass


@rutas_transacciones.delete("/transacciones{id_transacciones}", response_model=Transaccion)
async def eliminar_Transaccion(id_transaccion: int):
    pass