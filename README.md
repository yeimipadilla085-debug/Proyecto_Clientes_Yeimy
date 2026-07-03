#royecto: YeimyPadilla pro clientes

##Datos Personales
* **Nombre:** Yeimy Alejandra Padilla Gutierrez
* **Programa:**  Analisis y desarrollo de Software / 3407180
* **Fecha:** Mayo 26 2026



#PROYECTO_Clientes — API REST con FastAPI

API REST desarrollada con **FastAPI**, **SQLModel** y **SQLite** para la gestión de clientes, facturas y transacciones. Proyecto académico realizado como parte del programa de formación en el **SENA**, con el objetivo de poner en práctica el desarrollo de APIs REST, modelado relacional de datos y persistencia en base de datos con Python.

---

##Contexto académico

Este proyecto fue desarrollado durante el proceso de aprendizaje del programa de formación del SENA, como ejercicio práctico para aplicar los siguientes conceptos:

- Diseño y construcción de una API REST con FastAPI.
- Definición de modelos de datos y relaciones (uno a muchos) usando SQLModel.
- Persistencia de datos en una base de datos relacional (SQLite).
- Organización de un proyecto backend en módulos (enrutadores y modelos).
- Uso de control de versiones con Git y GitHub.

---

##Tecnologías utilizadas

- **Python 3.14**
- **FastAPI** — framework para construir la API
- **SQLModel** — ORM que combina SQLAlchemy y Pydantic para el modelado de datos
- **SQLite** — motor de base de datos relacional, usado en desarrollo
- **Pydantic v2** — validación de datos
- **Uvicorn** — servidor ASGI para ejecutar la aplicación

---

##Estructura del proyecto

```
PROYECTO_Clientes/
├── app/
│   ├── main.py                  # Punto de entrada de la API
│   ├── conexion_bd.py           # Configuración y conexión a la base de datos
│   ├── bd_clientes.squlite3     # Base de datos SQLite (generada automáticamente)
│   ├── enrutadores/
│   │   ├── clientes.py          # Rutas (endpoints) de Cliente
│   │   ├── facturas.py          # Rutas (endpoints) de Factura
│   │   └── transacciones.py     # Rutas (endpoints) de Transaccion
│   └── modelos/
│       ├── clientes.py          # Modelo de datos de Cliente
│       ├── facturas.py          # Modelo de datos de Factura
│       └── transacciones.py     # Modelo de datos de Transaccion
├── venv/                        # Entorno virtual (no incluido en git)
├── .gitignore
├── requeriments.txt
└── README.md
```

---

##Instalación y ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/yeimipadilla085-debug/YeimyPadilla_pro_cliente-py.git
cd nombre-pro-clientes
```

### 2. Crea y activa el entorno virtual

```bash
python -m venv venv
./venv/Scripts/activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Instala las dependencias

```bash
pip install -r requeriments.txt
```

### 4. Ejecuta el servidor

Desde la carpeta raíz del proyecto:

```bash
fastapi dev app/main.py
```

Al iniciar, la aplicación crea automáticamente la base de datos y sus tablas (si no existen todavía) en `app/bd_clientes.squlite3`.

### 5. Abre la documentación interactiva

```
http://127.0.0.1:8000/docs
```

Desde ahí puedes probar todos los endpoints directamente con la interfaz de **Swagger UI**.

---

#Endpoints disponibles

### Clientes

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/clientes` | Lista todos los clientes |
| GET | `/clientes/{cliente_id}` | Obtiene un cliente por ID |
| POST | `/clientes` | Crea un nuevo cliente |
| PATCH | `/clientes/{cliente_id}` | Edita un cliente existente |
| DELETE | `/clientes/{cliente_id}` | Elimina un cliente |

### Facturas

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/facturas` | Lista todas las facturas |
| GET | `/facturas/{factura_id}` | Obtiene una factura por ID |
| POST | `/facturas/{cliente_id}` | Crea una factura para un cliente |
| PATCH | `/facturas/{id_factura}` | Edita una factura |
| DELETE | `/facturas/{id_factura}` | Elimina una factura |

### Transacciones

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/transacciones` | Lista todas las transacciones |
| GET | `/transacciones/{id}` | Obtiene una transacción por ID |
| POST | `/transacciones/{factura_id}` | Crea una transacción asociada a una factura |
| PATCH | `/transacciones/{id}` | Edita una transacción |
| DELETE | `/transacciones/{id}` | Elimina una transacción |

---

#Modelos de datos

### Cliente
```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "email": "juan@email.com",
  "descripcion": "Cliente frecuente"
}
```

### Factura
```json
{
  "id": 1,
  "fecha": "2026-06-22",
  "cliente_id": 1,
  "cliente": { ... },
  "transacciones": [ ... ],
  "vr_total": 150000.0
}
```

### Transacción
```json
{
  "id": 1,
  "factura_id": 1,
  "cantidad": 3,
  "vr_unitario": 50000.0,
  "descripcion": "Detalle de la transacción"
}
```

---

##Relaciones entre entidades

- Un **Cliente** puede tener muchas **Facturas** (relación uno a muchos).
- Una **Factura** puede tener muchas **Transacciones** (relación uno a muchos).
- El campo `vr_total` de una **Factura** se calcula automáticamente como la suma de `cantidad * vr_unitario` de todas sus transacciones asociadas, mediante un `computed_field`.

---

##Notas

- Los datos se almacenan de forma persistente en una base de datos SQLite (`app/bd_clientes.squlite3`), no en memoria.
- Las tablas se crean automáticamente al iniciar la aplicación (`crear_tablas` en `conexion_bd.py`), siempre y cuando no existan previamente. Si se modifica un modelo (por ejemplo, se agrega una nueva columna), es necesario eliminar el archivo de base de datos para que se regenere con la nueva estructura, ya que el proyecto aún no implementa migraciones (por ejemplo, con Alembic).

