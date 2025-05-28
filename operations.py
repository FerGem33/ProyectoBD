from connection import get_connection

def obtener_datos():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM clientes")  # Cambia por tu tabla
        resultados = cursor.fetchall()
        conn.close()
        return resultados
    return []
