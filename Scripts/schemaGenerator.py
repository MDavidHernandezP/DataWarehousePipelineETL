# Database schema generator for various databases.

from db.mssqlClient import connect_to_mssql
from db.mysqlClient import connect_to_mysql
from db.oracleClient import connect_to_oracle
from db.postgresqlClient import connect_to_postgresql
from db.sqliteClient import connect_to_sqlite

from scriptExecutor import execute_sql_ddl_script

from pathlib import Path

def get_base_dir():
    return Path(__file__).resolve().parent.parent

def generate_schema_mssql():
    # Change these values according to your MsSQLServer setup.
    server = "localhost"    # Or the Docker container name if using Docker.
    database = "supermercado"
    username = "sa"
    password = "your_secure_password"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "DDL" / "MsSQLServer" / "rootTablesCreationQuery.sql"
    middle_script_path = BASE_DIR / "DDL" / "MsSQLServer" / "middleTablesCreationQuery.sql"
    last_script_path = BASE_DIR / "DDL" / "MsSQLServer" / "lastTablesCreationQuery.sql"

    connection = connect_to_mssql(server, database, username, password)

    if connection:
        execute_sql_ddl_script(connection, root_script_path)
        execute_sql_ddl_script(connection, middle_script_path)
        execute_sql_ddl_script(connection, last_script_path)
        connection.close()
        print("MsSQLServer connection closed.")
    else:
        print("Failed to connect to MsSQLServer.")

def generate_schema_mysql():
    # Change these values according to your MySQL setup.
    host = "localhost"    # Or the Docker container name if using Docker.
    user = "root"
    password = "yourpassword"
    database = "yourdatabase"
    
    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "DDL" / "MySQL" / "rootTablesCreationQuery.sql"
    middle_script_path = BASE_DIR / "DDL" / "MySQL" / "middleTablesCreationQuery.sql"
    last_script_path = BASE_DIR / "DDL" / "MySQL" / "lastTablesCreationQuery.sql"

    connection = connect_to_mysql(host, user, password, database)

    if connection:
        execute_sql_ddl_script(connection, root_script_path)
        execute_sql_ddl_script(connection, middle_script_path)
        execute_sql_ddl_script(connection, last_script_path)
        connection.close()
        print("MySQL connection closed.")
    else:
        print("Failed to connect to MySQL.")

def generate_schema_oracle():
    # Change these values according to your Oracle XE setup.
    host = "localhost"
    username = "sa"
    password = "your_secure_password"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "DDL" / "Oracle XE" / "rootTablesCreationQuery.sql"
    middle_script_path = BASE_DIR / "DDL" / "Oracle XE" / "middleTablesCreationQuery.sql"
    last_script_path = BASE_DIR / "DDL" / "Oracle XE" / "lastTablesCreationQuery.sql"

    connection = connect_to_oracle(username, password, host)

    if connection:
        execute_sql_ddl_script(connection, root_script_path)
        execute_sql_ddl_script(connection, middle_script_path)
        execute_sql_ddl_script(connection, last_script_path)
        connection.close()
        print("Oracle connection closed.")
    else:
        print("Failed to connect to Oracle.")

def generate_schema_postgresql():
    # Change these values according to your PostgreSQL setup.
    host = "localhost"
    database = "supermercado"
    user = "postgres"
    password = "your_secure_password"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "DDL" / "PostgreSQL" / "rootTablesCreationQuery.sql"
    middle_script_path = BASE_DIR / "DDL" / "PostgreSQL" / "middleTablesCreationQuery.sql"
    last_script_path = BASE_DIR / "DDL" / "PostgreSQL" / "lastTablesCreationQuery.sql"

    connection = connect_to_postgresql(host, user, password, database)

    if connection:
        execute_sql_ddl_script(connection, root_script_path)
        execute_sql_ddl_script(connection, middle_script_path)
        execute_sql_ddl_script(connection, last_script_path)
        connection.close()
        print("PostgreSQL connection closed.")
    else:
        print("Failed to connect to PostgreSQL.")

def generate_schema_sqlite():
    # Change these values according to your SQLite setup.
    database = "database.db"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "DDL" / "SQLite" / "rootTablesCreationQuery.sql"
    middle_script_path = BASE_DIR / "DDL" / "SQLite" / "middleTablesCreationQuery.sql"
    last_script_path = BASE_DIR / "DDL" / "SQLite" / "lastTablesCreationQuery.sql"

    connection = connect_to_sqlite(database)

    if connection:
        execute_sql_ddl_script(connection, root_script_path)
        execute_sql_ddl_script(connection, middle_script_path)
        execute_sql_ddl_script(connection, last_script_path)
        connection.close()
        print("SQLite connection closed.")
    else:
        print("Failed to connect to SQLite.")

if __name__ == "__main__":
    generate_schema_mssql()
    generate_schema_mysql()
    generate_schema_oracle()
    generate_schema_postgresql()
    generate_schema_sqlite()