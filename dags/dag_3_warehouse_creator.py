# Data warehouse creation DAG with Specific operator from Airflow.

from airflow import DAG
from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator
from datetime import datetime

with DAG("create_mssql_dwh", start_date=datetime(2024, 1, 1), schedule_interval=None, catchup=False) as dag:

    create_dwh = MsSqlOperator(
        task_id="create_dwh",
        mssql_conn_id="mssql_dwh_conn",  # Debes definir esta conexión en Airflow
        sql="sql/DDL/MsSQLServer/create_dwh.sql"
    )