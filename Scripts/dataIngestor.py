#

from db.mssqlClient import connect_to_mssql
from db.mysqlClient import connect_to_mysql
from db.oracleClient import connect_to_oracle
from db.postgresqlClient import connect_to_postgresql
from db.sqliteClient import connect_to_sqlite

from dataGenerator import generate_all_data

from scriptExecutor import execute_sql_dml_script

from pathlib import Path

def get_base_dir():
    return Path(__file__).resolve().parent.parent

def data_ingestor_mssql():
    # Change these values according to your MsSQLServer setup.
    server = "localhost"    # Or the Docker container name if using Docker.
    database = "supermercado"
    username = "sa"
    password = "your_secure_password"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "DML" / "MsSQLServer" / "rootTablesInsertionQuery.sql"
    middle_script_path = BASE_DIR / "DML" / "MsSQLServer" / "middleTablesInsertionQuery.sql"
    last_script_path = BASE_DIR / "DML" / "MsSQLServer" / "lastTablesInsertionQuery.sql"

    conn = connect_to_mssql(server, database, username, password)
    
    if conn:
        N = 10
        data = generate_all_data(N)
        print("Inserting data into MsSQLServer...")
        execute_sql_dml_script(conn, root_script_path, data, N)
        execute_sql_dml_script(conn, middle_script_path, data, N)
        execute_sql_dml_script(conn, last_script_path, data, N)
        print("Data inserted successfully into MsSQLServer.")
        conn.close()

def data_ingestor_mysql():
    # Change these values according to your MySQL setup.
    host = "localhost"    # Or the Docker container name if using Docker.
    user = "root"
    password = "yourpassword"
    database = "yourdatabase"
    
    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "DML" / "MySQL" / "rootTablesInsertionQuery.sql"
    middle_script_path = BASE_DIR / "DML" / "MySQL" / "middleTablesInsertionQuery.sql"
    last_script_path = BASE_DIR / "DML" / "MySQL" / "lastTablesInsertionQuery.sql"

    conn = connect_to_mysql(host, user, password, database)

    if conn:
        N = 10
        data = generate_all_data(N)
        print("Inserting data into MySQL...")
        execute_sql_dml_script(conn, root_script_path, data, N)
        execute_sql_dml_script(conn, middle_script_path, data, N)
        execute_sql_dml_script(conn, last_script_path, data, N)
        print("Data inserted successfully into MySQL.")
        conn.close()

def data_ingestor_oracle():
    # Change these values according to your Oracle XE setup.
    host = "localhost"    # Or the Docker container name if using Docker.
    username = "sa"
    password = "your_secure_password"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "DML" / "Oracle XE" / "rootTablesInsertionQuery.sql"
    middle_script_path = BASE_DIR / "DML" / "Oracle XE" / "middleTablesInsertionQuery.sql"
    last_script_path = BASE_DIR / "DML" / "Oracle XE" / "lastTablesInsertionQuery.sql"

    conn = connect_to_oracle(username, password, host)

    if conn:
        N = 10
        data = generate_all_data(N)
        print("Inserting data into Oracle...")
        execute_sql_dml_script(conn, root_script_path, data, N)
        execute_sql_dml_script(conn, middle_script_path, data, N)
        execute_sql_dml_script(conn, last_script_path, data, N)
        print("Data inserted successfully into Oracle.")
        conn.close()

def data_ingestor_postgresql():
    # Change these values according to your PostgreSQL setup.
    host = "localhost"    # Or the Docker container name if using Docker.
    database = "supermercado"
    user = "postgres"
    password = "your_secure_password"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "DML" / "PostgreSQL" / "rootTablesInsertionQuery.sql"
    middle_script_path = BASE_DIR / "DML" / "PostgreSQL" / "middleTablesInsertionQuery.sql"
    last_script_path = BASE_DIR / "DML" / "PostgreSQL" / "lastTablesInsertionQuery.sql"

    conn = connect_to_postgresql(host, user, password, database)

    if conn:
        N = 10
        data = generate_all_data(N)
        print("Inserting data into PostgreSQL...")
        execute_sql_dml_script(conn, root_script_path, data, N)
        execute_sql_dml_script(conn, middle_script_path, data, N)
        execute_sql_dml_script(conn, last_script_path, data, N)
        print("Data inserted successfully into PostgreSQL.")
        conn.close()

def data_ingestor_sqlite():
    # Change these values according to your SQLite setup.
    database = "supermercado.db"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "DML" / "SQLite" / "rootTablesInsertionQuery.sql"
    middle_script_path = BASE_DIR / "DML" / "SQLite" / "middleTablesInsertionQuery.sql"
    last_script_path = BASE_DIR / "DML" / "SQLite" / "lastTablesInsertionQuery.sql"

    conn = connect_to_sqlite(database)

    if conn:
        N = 10
        data = generate_all_data(N)
        print("Inserting data into SQLite...")
        execute_sql_dml_script(conn, root_script_path, data, N)
        execute_sql_dml_script(conn, middle_script_path, data, N)
        execute_sql_dml_script(conn, last_script_path, data, N)
        print("Data inserted successfully into SQLite.")
        conn.close()

if __name__ == "__main__":
    data_ingestor_mssql()
    data_ingestor_mysql()
    data_ingestor_oracle()
    data_ingestor_postgresql()
    data_ingestor_sqlite()