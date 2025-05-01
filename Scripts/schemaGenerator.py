# Database schema generator for various databases.

from db.mssqlClient import connect_to_mssql
from db.mysqlClient import connect_to_mysql
from db.oracleClient import connect_to_oracle
from db.postgresqlClient import connect_to_postgresql
from db.sqliteClient import connect_to_sqlite

from scriptExecutor import execute_sql_ddl_script

from config import get_mssql_config, get_mysql_config, get_oracle_config, get_postgresql_config, get_sqlite_config

from pathlib import Path

def get_base_dir():
    return Path(__file__).resolve().parent.parent

def generate_schema_mssql(server, database, username, password):
    # Change these values according to your MsSQLServer setup.
    server = server or "localhost"    # Or the Docker container name if using Docker.
    database = database or "supermercado"
    username = username or "sa"
    password = password or "your_secure_password"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "sql" / "DDL" / "MsSQLServer" / "rootTablesCreationQuery.sql"
    middle_script_path = BASE_DIR / "sql" / "DDL" / "MsSQLServer" / "middleTablesCreationQuery.sql"
    last_script_path = BASE_DIR / "sql" / "DDL" / "MsSQLServer" / "lastTablesCreationQuery.sql"

    connection = connect_to_mssql(server, database, username, password)

    if connection:
        execute_sql_ddl_script(connection, root_script_path)
        execute_sql_ddl_script(connection, middle_script_path)
        execute_sql_ddl_script(connection, last_script_path)
        connection.close()
        print("MsSQLServer connection closed.")
    else:
        print("Failed to connect to MsSQLServer.")

def generate_schema_mysql(host, user, password, database):
    # Change these values according to your MySQL setup.
    host = host or "localhost"    # Or the Docker container name if using Docker.
    user = user or "root"
    password = password or "yourpassword"
    database = database or "yourdatabase"
    
    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "sql" / "DDL" / "MySQL" / "rootTablesCreationQuery.sql"
    middle_script_path = BASE_DIR / "sql" / "DDL" / "MySQL" / "middleTablesCreationQuery.sql"
    last_script_path = BASE_DIR / "sql" / "DDL" / "MySQL" / "lastTablesCreationQuery.sql"

    connection = connect_to_mysql(host, user, password, database)

    if connection:
        execute_sql_ddl_script(connection, root_script_path)
        execute_sql_ddl_script(connection, middle_script_path)
        execute_sql_ddl_script(connection, last_script_path)
        connection.close()
        print("MySQL connection closed.")
    else:
        print("Failed to connect to MySQL.")

def generate_schema_oracle(username, password, host):
    # Change these values according to your Oracle XE setup.
    username = username or "sa"    # Or the Docker container name if using Docker.
    password = password or "your_secure_password"
    host = host or "localhost"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "sql" / "DDL" / "Oracle XE" / "rootTablesCreationQuery.sql"
    middle_script_path = BASE_DIR / "sql" / "DDL" / "Oracle XE" / "middleTablesCreationQuery.sql"
    last_script_path = BASE_DIR / "sql" / "DDL" / "Oracle XE" / "lastTablesCreationQuery.sql"

    connection = connect_to_oracle(username, password, host)

    if connection:
        execute_sql_ddl_script(connection, root_script_path)
        execute_sql_ddl_script(connection, middle_script_path)
        execute_sql_ddl_script(connection, last_script_path)
        connection.close()
        print("Oracle connection closed.")
    else:
        print("Failed to connect to Oracle.")

def generate_schema_postgresql(host, user, password, database):
    # Change these values according to your PostgreSQL setup.
    host = host or "localhost"    # Or the Docker container name if using Docker.
    user = user or "postgres"
    password = password or "your_secure_password"
    database = database or "supermercado"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "sql" / "DDL" / "PostgreSQL" / "rootTablesCreationQuery.sql"
    middle_script_path = BASE_DIR / "sql" / "DDL" / "PostgreSQL" / "middleTablesCreationQuery.sql"
    last_script_path = BASE_DIR / "sql" / "DDL" / "PostgreSQL" / "lastTablesCreationQuery.sql"

    connection = connect_to_postgresql(host, user, password, database)

    if connection:
        execute_sql_ddl_script(connection, root_script_path)
        execute_sql_ddl_script(connection, middle_script_path)
        execute_sql_ddl_script(connection, last_script_path)
        connection.close()
        print("PostgreSQL connection closed.")
    else:
        print("Failed to connect to PostgreSQL.")

def generate_schema_sqlite(database):
    # Change these values according to your SQLite setup.
    database = database or "supermercado.db"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "sql" / "DDL" / "SQLite" / "rootTablesCreationQuery.sql"
    middle_script_path = BASE_DIR / "sql" / "DDL" / "SQLite" / "middleTablesCreationQuery.sql"
    last_script_path = BASE_DIR / "sql" / "DDL" / "SQLite" / "lastTablesCreationQuery.sql"

    connection = connect_to_sqlite(database)

    if connection:
        execute_sql_ddl_script(connection, root_script_path)
        execute_sql_ddl_script(connection, middle_script_path)
        execute_sql_ddl_script(connection, last_script_path)
        connection.close()
        print("SQLite connection closed.")
    else:
        print("Failed to connect to SQLite.")

def main():
    # Load configurations.
    mssql_cfg = get_mssql_config()
    mysql_cfg = get_mysql_config()
    oracle_cfg = get_oracle_config()
    postgresql_cfg = get_postgresql_config()
    sqlite_cfg = get_sqlite_config()

    # Example usage:
    generate_schema_mssql(mssql_cfg["server"], mssql_cfg["database"], mssql_cfg["username"], mssql_cfg["password"])
    generate_schema_mysql(mysql_cfg["host"], mysql_cfg["user"], mysql_cfg["password"], mysql_cfg["database"])
    generate_schema_oracle(oracle_cfg["username"], oracle_cfg["password"], oracle_cfg["host"])
    generate_schema_postgresql(postgresql_cfg["host"], postgresql_cfg["user"], postgresql_cfg["password"], postgresql_cfg["database"])
    generate_schema_sqlite(sqlite_cfg["database"])

if __name__ == "__main__":
    main()