from fastapi import APIRouter, HTTPException, status
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from listas import lista_clientes 
from conexion_bd import Session_dependencia
from sqlmodel import select

rutas_clientes = APIRouter()  
#lista_clientes: list[Cliente] = []


@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes(sesion: Session_dependencia):
    lista_cli = sesion.exec(select(Cliente)).all()
    return lista_cli


@rutas_clientes.get(
        "/clientes/{cliente_id}", 
        response_model=Cliente)

async def listar_cliente(cliente_id: int, mi_sesion: Session_dependencia):
    Cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not Cliente_bd:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"El cliente con id{cliente_id}, no esxiste,"
    )
    return Cliente_bd


@rutas_clientes.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear, mi_sesion: Session_dependencia):
    Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(Cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh(Cliente_val)
    return Cliente_val


@rutas_clientes.patch("/clientes{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar, mi_sesion: Session_dependencia):
    Cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not Cliente_bd:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"El cliente con id{cliente_id}, no esxiste,"
    )
    Cliente_dict = datos_cliente.model_dump(exclude_unset=True)
    Cliente_bd.sqlmodel_update(Cliente_dict)
    mi_sesion.add(Cliente_bd)
    mi_sesion.commit()
    mi_sesion.refresh(Cliente_bd)
    return Cliente_bd


@rutas_clientes.delete("/clientes{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int, mi_sesion: Session_dependencia):
    Cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not Cliente_bd:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"El cliente con id{cliente_id}, no esxiste,"
    )
    mi_sesion.delete(Cliente_bd)
    mi_sesion.commit()
    
    return Cliente_bd
