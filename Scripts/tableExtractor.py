# Data extractor script for multiple databases.

from db.mssqlClient import connect_to_mssql
from db.mysqlClient import connect_to_mysql
from db.oracleClient import connect_to_oracle
from db.postgresqlClient import connect_to_postgresql
from db.sqliteClient import connect_to_sqlite

from config import get_mssql_config, get_mysql_config, get_oracle_config, get_postgresql_config, get_sqlite_config

import pandas as pd

def table_extractor_mssql(server, database, username, password, table_name):
    # Change these values according to your MsSQLServer setup.
    server = server or "localhost"    # Or the Docker container name if using Docker.
    database = database or "your_database"
    username = username or "sa"
    password = password or "your_secure_password"

    conn = connect_to_mssql(server, database, username, password)

    if conn:
        try:
            df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
            return df
        except Exception as e:
            print(f"[ERROR] Failed to read table {table_name} from MSSQL: {e}")
            return None
        finally:
            conn.close()
    else:
        print("[ERROR] Could not establish MSSQL connection.")
        return None

def table_extractor_mysql(host, user, password, database, table_name):
    # Change these values according to your MySQL setup.
    host = host or "localhost"    # Or the Docker container name if using Docker.
    user = user or "root"
    password = password or "your_secure_password"
    database = database or "your_database"

    conn = connect_to_mysql(host, user, password, database)

    if conn:
        try:
            df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
            return df
        except Exception as e:
            print(f"[ERROR] Failed to read table {table_name} from MySQL: {e}")
            return None
        finally:
            conn.close()
    else:
        print("[ERROR] Could not establish MySQL connection.")
        return None
    
def table_extractor_oracle(username, password, host, table_name):
    # Change these values according to your Oracle XE setup.
    username = username or "sa"
    password = password or "your_secure_password"
    host = host or "localhost"    # Or the Docker container name if using Docker.

    conn = connect_to_oracle(username, password, host)

    if conn:
        try:
            df = pd.read_sql(f'SELECT * FROM "{table_name}"', conn)
            return df
        except Exception as e:
            print(f"[ERROR] Failed to read table {table_name} from Oracle: {e}")
            return None
        finally:
            conn.close()
    else:
        print("[ERROR] Could not establish Oracle connection.")
        return None
    
def table_extractor_postgresql(host, user, password, database, table_name):
    # Change these values according to your PostgreSQL setup.
    host = host or "localhost"    # Or the Docker container name if using Docker.
    user = user or "postgres"
    password = password or "your_secure_password"
    database = database or "your_database"

    conn = connect_to_postgresql(host, user, password, database)

    if conn:
        try:
            df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
            return df
        except Exception as e:
            print(f"[ERROR] Failed to read table {table_name} from PostgreSQL: {e}")
            return None
        finally:
            conn.close()
    else:
        print("[ERROR] Could not establish PostgreSQL connection.")
        return None
    
def table_extractor_sqlite(database, table_name):
    # Change these values according to your SQLite setup.
    database = database or "your_database.db"

    conn = connect_to_sqlite(database)
    
    if conn:
        try:
            df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
            return df
        except Exception as e:
            print(f"[ERROR] Failed to read table {table_name} from SQLite: {e}")
            return None
        finally:
            conn.close()
    else:
        print("[ERROR] Could not establish SQLite connection.")
        return None

def main():
    # Load configurations.
    mssql_config = get_mssql_config()
    mysql_config = get_mysql_config()
    oracle_config = get_oracle_config()
    postgresql_config = get_postgresql_config()
    sqlite_config = get_sqlite_config()

    # Example usage:
    mssql_data = table_extractor_mssql(**mssql_config, table_name="your_table_name")
    mysql_data = table_extractor_mysql(**mysql_config, table_name="your_table_name")
    oracle_data = table_extractor_oracle(**oracle_config, table_name="your_table_name")
    postgresql_data = table_extractor_postgresql(**postgresql_config, table_name="your_table_name")
    sqlite_data = table_extractor_sqlite(**sqlite_config, table_name="your_table_name")

if __name__ == "__main__":
    main()