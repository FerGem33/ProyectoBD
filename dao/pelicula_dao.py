from connection import get_connection

def obtener_peliculas():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pelicula")
        peliculas = cursor.fetchall()
        conn.close()
        return peliculas
    return []

def agregar_pelicula(nombre, clasificacion, duracion, idgenero, idactor, idirector):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Pelicula (NOMBRE, CLASIFICACION, DURACION, IDGENERO, IDACTOR, IDDIRECTOR)
            VALUES (:1, :2, :3, :4, :5, :6)
        """, (nombre, clasificacion, duracion, idgenero, idactor, idirector))
        conn.commit()
        conn.close()

def actualizar_pelicula(id, nombre, clasificacion, duracion, idgenero, idactor, iddirector):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Pelicula
            SET nombre = :1, clasificacion = :2, duracion = :3,
                idgenero = :4, idactor = :5, iddirector = :6
            WHERE idPelicula = :7
        """, (nombre, clasificacion, duracion, idgenero, idactor, iddirector, id))
        conn.commit()
        conn.close()


def eliminar_pelicula(id):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Pelicula WHERE idPelicula = :1", (id,))
        conn.commit()
        conn.close()
