from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine
import os

carpeta_actual = os.path.dirname(os.path.abspath(__file__))
nombre_bd = "bd_clientes.squlite3"
ruta_bd = os.path.join(carpeta_actual, nombre_bd)
url_bd = f"sqlite:///{ruta_bd}"

motor_bd = create_engine(url_bd)


def crear_tablas(app: FastAPI):
    SQLModel.metadata.create_all(motor_bd)
    yield


def obtener_sesion():
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion


Session_dependencia = Annotated[Session, Depends(obtener_sesion)]