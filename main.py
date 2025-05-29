from connection import get_connection
from ui import crear_interfaz

if __name__ == "__main__":
    conn = get_connection
    if conn: 
        print("Conexión exitosa con la base de datos!")
        crear_interfaz
    
