from connection import get_connection

def obtener_generos():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT idGenero, descripcion FROM Genero")
        generos = cursor.fetchall()
        conn.close()
        return generos
    return []

def obtener_genero(id):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT descripcion FROM Genero WHERE idGenero = {} ".format(id))
        genero = cursor.fetchall()
        conn.close()
        return str(genero)[3:-4]
    return None
