# Data ingestor script for multiple databases.

from db.mssqlClient import connect_to_mssql
from db.mysqlClient import connect_to_mysql
from db.oracleClient import connect_to_oracle
from db.postgresqlClient import connect_to_postgresql
from db.sqliteClient import connect_to_sqlite

from dataGenerator import generate_all_data

from scriptExecutor import execute_sql_dml_script

from config import get_mssql_config, get_mysql_config, get_oracle_config, get_postgresql_config, get_sqlite_config

from pathlib import Path

def get_base_dir():
    return Path(__file__).resolve().parent.parent

def data_ingestor_mssql(server, database, username, password, N):
    # Change these values according to your MsSQLServer setup.
    server = server or "localhost"    # Or the Docker container name if using Docker.
    database = database or "your_database"
    username = username or "sa"
    password = password or "your_secure_password"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "sql" / "DML" / "MsSQLServer" / "rootTablesInsertionQuery.sql"
    middle_script_path = BASE_DIR / "sql" / "DML" / "MsSQLServer" / "middleTablesInsertionQuery.sql"
    last_script_path = BASE_DIR / "sql" / "DML" / "MsSQLServer" / "lastTablesInsertionQuery.sql"

    conn = connect_to_mssql(server, database, username, password)
    
    if conn:
        data = generate_all_data(N)
        print("Inserting data into MsSQLServer...")
        execute_sql_dml_script(conn, root_script_path, data, N)
        execute_sql_dml_script(conn, middle_script_path, data, N)
        execute_sql_dml_script(conn, last_script_path, data, N)
        print("Data inserted successfully into MsSQLServer.")
        conn.close()

def data_ingestor_mysql(host, user, password, database, N):
    # Change these values according to your MySQL setup.
    host = host or "localhost"    # Or the Docker container name if using Docker.
    user = user or "root"
    password = password or "your_secure_password"
    database = database or "your_database"
    
    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "sql" / "DML" / "MySQL" / "rootTablesInsertionQuery.sql"
    middle_script_path = BASE_DIR / "sql" / "DML" / "MySQL" / "middleTablesInsertionQuery.sql"
    last_script_path = BASE_DIR / "sql" / "DML" / "MySQL" / "lastTablesInsertionQuery.sql"

    conn = connect_to_mysql(host, user, password, database)

    if conn:
        data = generate_all_data(N)
        print("Inserting data into MySQL...")
        execute_sql_dml_script(conn, root_script_path, data, N)
        execute_sql_dml_script(conn, middle_script_path, data, N)
        execute_sql_dml_script(conn, last_script_path, data, N)
        print("Data inserted successfully into MySQL.")
        conn.close()

def data_ingestor_oracle(host, username, password, N):
    # Change these values according to your Oracle XE setup.
    username = username or "sa"
    password = password or "your_secure_password"
    host = host or "localhost"    # Or the Docker container name if using Docker.

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "sql" / "DML" / "Oracle XE" / "rootTablesInsertionQuery.sql"
    middle_script_path = BASE_DIR / "sql" / "DML" / "Oracle XE" / "middleTablesInsertionQuery.sql"
    last_script_path = BASE_DIR / "sql" / "DML" / "Oracle XE" / "lastTablesInsertionQuery.sql"

    conn = connect_to_oracle(username, password, host)

    if conn:
        data = generate_all_data(N)
        print("Inserting data into Oracle...")
        execute_sql_dml_script(conn, root_script_path, data, N)
        execute_sql_dml_script(conn, middle_script_path, data, N)
        execute_sql_dml_script(conn, last_script_path, data, N)
        print("Data inserted successfully into Oracle.")
        conn.close()

def data_ingestor_postgresql(host, user, password, database, N):
    # Change these values according to your PostgreSQL setup.
    host = host or "localhost"    # Or the Docker container name if using Docker.
    user = user or "postgres"
    password = password or "your_secure_password"
    database = database or "your_database"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "sql" / "DML" / "PostgreSQL" / "rootTablesInsertionQuery.sql"
    middle_script_path = BASE_DIR / "sql" / "DML" / "PostgreSQL" / "middleTablesInsertionQuery.sql"
    last_script_path = BASE_DIR / "sql" / "DML" / "PostgreSQL" / "lastTablesInsertionQuery.sql"

    conn = connect_to_postgresql(host, user, password, database)

    if conn:
        data = generate_all_data(N)
        print("Inserting data into PostgreSQL...")
        execute_sql_dml_script(conn, root_script_path, data, N)
        execute_sql_dml_script(conn, middle_script_path, data, N)
        execute_sql_dml_script(conn, last_script_path, data, N)
        print("Data inserted successfully into PostgreSQL.")
        conn.close()

def data_ingestor_sqlite(database, N):
    # Change these values according to your SQLite setup.
    database = database or "your_database.db"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "sql" / "DML" / "SQLite" / "rootTablesInsertionQuery.sql"
    middle_script_path = BASE_DIR / "sql" / "DML" / "SQLite" / "middleTablesInsertionQuery.sql"
    last_script_path = BASE_DIR / "sql" / "DML" / "SQLite" / "lastTablesInsertionQuery.sql"

    conn = connect_to_sqlite(database)

    if conn:
        data = generate_all_data(N)
        print("Inserting data into SQLite...")
        execute_sql_dml_script(conn, root_script_path, data, N)
        execute_sql_dml_script(conn, middle_script_path, data, N)
        execute_sql_dml_script(conn, last_script_path, data, N)
        print("Data inserted successfully into SQLite.")
        conn.close()

def main():
    # Load configurations.
    mssql_config = get_mssql_config()
    mysql_config = get_mysql_config()
    oracle_config = get_oracle_config()
    postgresql_config = get_postgresql_config()
    sqlite_config = get_sqlite_config()

    # Number of records to generate.
    N = 50

    # Example usage:
    data_ingestor_mssql(**mssql_config, N=N)
    data_ingestor_mysql(**mysql_config, N=N)
    data_ingestor_oracle(**oracle_config, N=N)
    data_ingestor_postgresql(**postgresql_config, N=N)
    data_ingestor_sqlite(**sqlite_config, N=N)

if __name__ == "__main__":
    main()