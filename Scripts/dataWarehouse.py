# Data Warehouse creator script for MsSQLServer.

from db.mssqlClient import connect_to_mssql

from scriptExecutor import execute_sql_ddl_script

from config import get_mssql_config

from pathlib import Path

import pandas as pd

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

def load_tables_data_warehouse(server, database, username, password, table_name, schema_name, df: pd.DataFrame):
    # Change these values according to your MsSQLServer setup.
    server = server or "localhost"    # Or the Docker container name if using Docker.
    database = database or "your_database"
    username = username or "sa"
    password = password or "your_secure_password"

    if df is None or df.empty:
        print(f"[INFO] No data to insert into {schema_name}.{table_name}. DataFrame is empty.")
        return

    connection = connect_to_mssql(server, database, username, password)

    if connection:
        cursor = connection.cursor()
        cursor.fast_executemany = True

        columns = ', '.join(df.columns)
        placeholders = ', '.join(['?'] * len(df.columns))
        sql = f"INSERT INTO {schema_name}.{table_name} ({columns}) VALUES ({placeholders})"

        try:
            cursor.executemany(sql, df.values.tolist())
            connection.commit()
            print(f"Inserted {len(df)} rows into {schema_name}.{table_name}")
        except Exception as e:
            print(f"Error inserting data: {e}")
        finally:
            connection.close()
            print("MsSQLServer connection closed.")
    else:
        print("Failed to connect to MsSQLServer.")

def main():
    # Get the configuration from the config module.
    mssql_cfg = get_mssql_config()
    generate_schema_data_warehouse(**mssql_cfg)

    # Example DataFrame to load into the data warehouse.
    df = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': ['A', 'B', 'C']
    })

    # Load the DataFrame into the data warehouse.
    load_tables_data_warehouse(
        server=mssql_cfg['server'],
        database=mssql_cfg['database'],
        username=mssql_cfg['username'],
        password=mssql_cfg['password'],
        table_name='your_table_name',
        schema_name='your_schema_name',
        df=df
    )

if __name__ == "__main__":
    main()