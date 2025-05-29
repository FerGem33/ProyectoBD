from connection import get_connection

def obtener_actores():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Actor")
        actores = cursor.fetchall()
        conn.close()
        return actores
    return []

def obtener_actor(id):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nombre ||' '|| apellido FROM Actor WHERE idactor = {}".format(id))
        actor = cursor.fetchall()
        conn.close()
        return str(actor)[3:-4]
    return None

def agregar_actor(nombre):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Actor (nombre) VALUES (:1)", (nombre,))
        conn.commit()
        conn.close()

def actualizar_actor(id, nombre):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Actor SET nombre = :1 WHERE idActor = :2", (nombre, id))
        conn.commit()
        conn.close()

def eliminar_actor(id):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Actor WHERE idActor = :1", (id,))
        conn.commit()
        conn.close()
