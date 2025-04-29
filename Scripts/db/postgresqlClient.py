import psycopg2

def connect_to_postgresql(host, user, password, database, port=5432):
    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        return conn
    except Exception as e:
        print("Error connecting to PostgreSQL:", e)
        return None
