# 🎬 Oracle Tkinter App

Aplicación en **Python** que se conecta a **Oracle Database** usando `oracledb` y proporciona una interfaz gráfica con `Tkinter` para la gestión de películas, géneros, actores y directores.

---

## 🚀 Requisitos

- Python 3.8 o superior
- Oracle Database (como Oracle XE)
- Paquete [`oracledb`](https://pypi.org/project/oracledb/)
- Acceso a la base de datos configurado (usuario, contraseña)

---

## 📦 Instalación

1. Clona el repositorio o descarga el proyecto:

```bash
git clone https://github.com/FerGem33/ProyectoBD.git
cd src
```
Instala las dependencias:

```bash
pip install -r requirements.txt
```
## 🗃️ Configuración de la Base de Datos
En la carpeta sql/ se encuentran dos archivos importantes:

`crear.sql`: Crea las tablas Genero, Actor, Director, y Pelicula.

`llenar.sql`: Llena las tablas con registros de ejemplo (géneros, actores, directores, películas).

## 💾 Ejecución en SQL*Plus o SQL Developer
Puedes ejecutar ambos archivos en tu cliente de Oracle:

```sql
@sql/crear.sql
@sql/llenar.sql
```
Asegúrate de conectarte con el usuario correcto antes de ejecutar los scripts.

## 🖥️ Ejecutar la Aplicación
Una vez que tengas la base de datos lista:

```bash
python main.py
```
Esto abrirá una ventana con la interfaz gráfica.

📁 Estructura del Proyecto
```bash
├── main.py                # Código principal de la interfaz Tkinter
├── db.py                  # Módulo de conexión a Oracle
├── sql/
│   ├── crear.sql          # Script para crear las tablas
│   └── llenar.sql         # Script para insertar datos iniciales
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Este archivo
```