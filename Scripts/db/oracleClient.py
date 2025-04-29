import cx_Oracle

def connect_to_oracle(username, password, host, port=1521, service_name="XE"):
    try:
        dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
        conn = cx_Oracle.connect(user=username, password=password, dsn=dsn)
        return conn
    except Exception as e:
        print("Error connecting to Oracle:", e)
        return None