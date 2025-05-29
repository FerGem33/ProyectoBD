import oracledb

def get_connection():
    try:
        connection = oracledb.connect(
            user="proyecto2",
            password="proyecto2",
            dsn="localhost:1522/XEPDB1"
        )        
        return connection
    
    except oracledb.Error as e:
        print(e)
        return None
