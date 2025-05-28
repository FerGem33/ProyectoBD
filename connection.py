import oracledb

def get_connection():
    try:
        # Modo "Thin" predeterminado no necesita Oracle Client
        connection = oracledb.connect(
            user="usuario",
            password="contraseña",
            dsn="localhost/XE"  # Formato simplificado: host/servicio
        )
        print("Conexión exitosa")
        return connection
    except oracledb.Error as e:
        print(f"Error al conectar a Oracle: {e}")
        return None
