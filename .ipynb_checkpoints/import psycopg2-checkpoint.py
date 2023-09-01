import psycopg2

config = {
    "user": "admin",
    "password": "admin",
    "database": "etl_db"
}

def create_connection():
    try:
        cnx = psycopg2.connect(
            host='localhost',
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        print('Conexión exitosa!!')
    except psycopg2.Error as e:
        cnx = None
        print('No se puede conectar:', e)
    return cnx

if __name__ == "__main__":
    create_connection()
