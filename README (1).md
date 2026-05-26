# Proyecto: nombre-pro-clientes

#Datos del Aprendis 

| Nombre    | Juan Felipe Zapata Torres           |
| Correo    | JF4979735@gmail.com                 |
| Ciudad    | Bogotá, Colombia                    |
| Fecha     | 25/05/2026                          |



#Descripción

API REST construida con *Python* y *FastAPI* que expone dos endpoints:

`GET /` — Retorna un mensaje de bienvenida del proyecto.
`GET /clientes` — Retorna una lista de clientes registrados.


#intalacion de:

[Python](https://www.python.org/)

#Paso a paso de ejecución

#1. Crear la carpeta del proyecto

```
mkdir nombre-pro-clientes
```

Crea una nueva carpeta llamada `nombre-pro-clientes`


#2. Entrar a la carpeta

```
cd nombre-pro-clientes
```


#3. Crear el entorno virtual

```
python -m venv venv
```

Crea un entorno virtual llamado `venv` dentro del proyecto. Esto aísla las librerías del proyecto del resto del sistema.


#4. Activar el entorno virtual

```
venv\Scripts\activate
```

Cuando el entornom se activo, observe `(venv)` al inicio de mi terminal.


#5. Instalar las dependencias

```
pip install fastapi uvicorn
```

Instala dos librerías:
- **fastapi** — framework para crear la API REST.
- **uvicorn** — servidor que ejecuta la aplicación FastAPI.


#6. Crear el archivo principal

```
touch main.py
```

#7. Ejecutar el servidor

```
uvicorn main:app --reload
```

Inicia el servidor *http://127.0.0.1:8000*.


#8. Probar los endpoints

Abri el navegador y probe:

| Método | URL                               | Descripción           |
|--------|-----------------------------------|-----------------------|
| GET    | http://localhost:8000/            | Mensaje de bienvenida |
| GET    | http://localhost:8000/clientes    | Lista de clientes     |

por alguna razon no me genero el http://127.0.0.1:8000/docs , ya que tuve que agragar el "/docs" manualmente

#ejempo de el navegaror

#GET /

```json
{
  "mensaje": "este es el proyecto de clientes a desarrollar"
}
```

#GET /clientes

```json
{
  "status": "success",
  "total": 7,
  "data": [
    {"id": 1, "nombre": "Maria Esperanza",  "email": "Espe@email.com",  "ciudad": "Bogotá",       "telefono": "300-111-2233"},
        {"id": 2, "nombre": "Juan Felipe",     "email": "jf49@email.com",     "ciudad": "Bogotá",     "telefono": "311-222-3344"},
  ]
}
```



#Estructura del proyecto

```
nombre-pro-clientes/
├── main.py        
├── README.md       
└── venv/            
```

#Tecnologías usadas

- **Python** — Lenguaje de programación
- **FastAPI** — Framework para crear APIs REST modernas
- **Uvicorn** — Servidor ASGI para ejecutar FastAPI
