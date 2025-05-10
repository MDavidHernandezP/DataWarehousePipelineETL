# Data Warehouse creator script for MsSQLServer.

from scripts.db.mssqlClient import connect_to_mssql

from scripts.scriptExecutor import execute_sql_ddl_script

from scripts.tableExtractor import table_extractor_mssql, table_extractor_mysql, table_extractor_oracle, table_extractor_postgresql, table_extractor_sqlite

from config import get_data_warehouse_config, get_mssql_config, get_mysql_config, get_oracle_config, get_postgresql_config, get_sqlite_config

from pathlib import Path

from pandas import notnull

def get_base_dir():
    return Path(__file__).resolve().parent.parent

def generate_schema_data_warehouse(server, database, username, password):
    # Change these values according to your MsSQLServer setup.
    server = server or "localhost"    # Or the Docker container name if using Docker.
    database = database or "your_database"
    username = username or "sa"
    password = password or "your_secure_password"

    # Paths to the SQL scripts.
    BASE_DIR = get_base_dir()
    root_script_path = BASE_DIR / "sql" / "DDL" / "MsSQLServer" / "dataWarehouseCreationQuery.sql"

    connection = connect_to_mssql(server, database, username, password)

    if connection:
        execute_sql_ddl_script(connection, root_script_path)
        connection.close()
        print("MsSQLServer connection closed.")
    else:
        print("Failed to connect to MsSQLServer.")

def table_loader_to_bronze_layer(table_name, df):
    # Get the Data Warehouse configuration from the config module.
    data_warehouse_cfg = get_data_warehouse_config()

    # Convert NaN/NaT to None to avoid issues with executemany.
    df = df.where(notnull(df), None)

    # Connect and load tables extracted to the MsSQLServer Data Warehouse.
    try:
        connection = connect_to_mssql(data_warehouse_cfg['server'], data_warehouse_cfg['database'], data_warehouse_cfg['username'], data_warehouse_cfg['password'])
        if connection:
            cursor = connection.cursor()
            cursor.fast_executemany = True

            # Escape column names with brackets to avoid SQL Server issues.
            columns = ', '.join([f"[{col}]" for col in df.columns])
            placeholders = ', '.join(['?'] * len(df.columns))
            sql = f"INSERT INTO {'bronze'}.{table_name} ({columns}) VALUES ({placeholders})"

            try:
                cursor.executemany(sql, df.values.tolist())
                connection.commit()
                print(f"Inserted {len(df)} rows into {'bronze'}.{table_name}")
            except Exception as e:
                print(f"Error inserting data: {e}")
            finally:
                connection.close()
                print("MsSQLServer Data Warehouse connection closed.")
        else:
            print("Failed to connect to MsSQLServer Data Warehouse.")
    except Exception as e:
        print(f"[ERROR] Exception occurred while connecting to MsSQLServer Data Warehouse: {e}")
        return

def load_mssql_tables(server, database, username, password, table_name):
    table_name = table_name or "your_table_name"
    
    # Change these values according to your MsSQLServer setup.
    server = server or "localhost"    # Or the Docker container name if using Docker.
    database = database or "your_database"
    username = username or "sa"
    password = password or "your_secure_password"

    # Extract data from MsSQLServer and load it into the bronze layer.
    try:
        mssql_df = table_extractor_mssql(server, database, username, password, table_name)
        if mssql_df is not None:
            print(f"Extracted {len(mssql_df)} rows from {table_name} in MsSQLServer.")
            table_loader_to_bronze_layer(table_name, mssql_df)
        else:
            print(f"[ERROR] Failed to extract data from {table_name} in MsSQLServer.")
            return
    except Exception as e:
        print(f"[ERROR] Exception occurred while extracting data from MsSQLServer: {e}")
        return
    
def load_mysql_tables(host, user, password, database, table_name):
    table_name = table_name or "your_table_name"
    
    # Change these values according to your MySQL setup.
    host = host or "localhost"    # Or the Docker container name if using Docker.
    user = user or "root"
    password = password or "your_secure_password"
    database = database or "your_database"

    # Extract data from MySQL and load it into the bronze layer.
    try:
        mysql_df = table_extractor_mysql(host, user, password, database, table_name)
        if mysql_df is not None:
            print(f"Extracted {len(mysql_df)} rows from {table_name} in MySQL.")
            table_loader_to_bronze_layer(table_name, mysql_df)
        else:
            print(f"[ERROR] Failed to extract data from {table_name} in MySQL.")
            return
    except Exception as e:
        print(f"[ERROR] Exception occurred while extracting data from MySQL: {e}")
        return
    
def load_oracle_tables(username, password, host, table_name):
    table_name = table_name or "your_table_name"
    
    # Change these values according to your Oracle XE setup.
    username = username or "sa"
    password = password or "your_secure_password"
    host = host or "localhost"    # Or the Docker container name if using Docker.

    # Extract data from Oracle and load it into the bronze layer.
    try:
        oracle_df = table_extractor_oracle(username, password, host, table_name)
        if oracle_df is not None:
            print(f"Extracted {len(oracle_df)} rows from {table_name} in Oracle.")
            table_loader_to_bronze_layer(table_name, oracle_df)
        else:
            print(f"[ERROR] Failed to extract data from {table_name} in Oracle.")
            return
    except Exception as e:
        print(f"[ERROR] Exception occurred while extracting data from Oracle: {e}")
        return
    
def load_postgresql_tables(host, user, password, database, table_name):
    table_name = table_name or "your_table_name"
    
    # Change these values according to your PostgreSQL setup.
    host = host or "localhost"    # Or the Docker container name if using Docker.
    user = user or "postgres"
    password = password or "your_secure_password"
    database = database or "your_database"

    # Extract data from PostgreSQL and load it into the bronze layer.
    try:
        postgresql_df = table_extractor_postgresql(host, user, password, database, table_name)
        if postgresql_df is not None:
            print(f"Extracted {len(postgresql_df)} rows from {table_name} in PostgreSQL.")
            table_loader_to_bronze_layer(table_name, postgresql_df)
        else:
            print(f"[ERROR] Failed to extract data from {table_name} in PostgreSQL.")
            return
    except Exception as e:
        print(f"[ERROR] Exception occurred while extracting data from PostgreSQL: {e}")
        return
    
def load_sqlite_tables(database, table_name):
    table_name = table_name or "your_table_name"
    
    # Change these values according to your SQLite setup.
    database = database or "your_database.db"

    # Extract data from SQLite and load it into the bronze layer.
    try:
        sqlite_df = table_extractor_sqlite(database, table_name)
        if sqlite_df is not None:
            print(f"Extracted {len(sqlite_df)} rows from {table_name} in SQLite.")
            table_loader_to_bronze_layer(table_name, sqlite_df)
        else:
            print(f"[ERROR] Failed to extract data from {table_name} in SQLite.")
            return
    except Exception as e:
        print(f"[ERROR] Exception occurred while extracting data from SQLite: {e}")
        return

def main():
    # Get the configuration from the config module.
    mssql_cfg = get_mssql_config()
    mysql_cfg = get_mysql_config()
    oracle_cfg = get_oracle_config()
    postgresql_cfg = get_postgresql_config()
    sqlite_cfg = get_sqlite_config()

    # Generate the Data Warehouse schema.
    generate_schema_data_warehouse(**mssql_cfg)

    # Load tables from different databases into the bronze layer.
    load_mssql_tables(**mssql_cfg, table_name="your_table_name")
    load_mysql_tables(**mysql_cfg, table_name="your_table_name")
    load_oracle_tables(**oracle_cfg, table_name="your_table_name")
    load_postgresql_tables(**postgresql_cfg, table_name="your_table_name")
    load_sqlite_tables(**sqlite_cfg, table_name="your_table_name")

if __name__ == "__main__":
    main()