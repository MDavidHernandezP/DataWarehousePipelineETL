from db.mssqlClient import connect_to_mssql

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

if __name__ == "__main__":
    ()