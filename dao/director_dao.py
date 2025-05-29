from connection import get_connection

def obtener_directores():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Director")
        directores = cursor.fetchall()
        conn.close()
        return directores
    return []

def obtener_director(id):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nombre||' '||apellido FROM Director WHERE iddirector = {}".format(id))
        director = cursor.fetchall()
        conn.close()
        return str(director)[3:-4]
    return None

def agregar_director(nombre):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Director (nombre) VALUES (:1)", (nombre,))
        conn.commit()
        conn.close()

def actualizar_director(id, nombre):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Director SET nombre = :1 WHERE idDirector = :2", (nombre, id))
        conn.commit()
        conn.close()

def eliminar_director(id):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Director WHERE idDirector = :1", (id,))
        conn.commit()
        conn.close()