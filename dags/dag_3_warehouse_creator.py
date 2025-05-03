# Data warehouse creation DAG with Specific operator from Airflow.
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from scripts.dataWarehouse import generate_schema_data_warehouse
from config import get_mssql_config

dag = DAG(
    'dag_2_data_ingestor',
    default_args={
        'owner': 'airflow',
        'start_date': '2025-05-01',
        'retries': 1,
    },
    schedule_interval=None,
    catchup=False
)

create_data_warehouse_task = PythonOperator(
    task_id='create_data_warehouse_task',
    python_callable=generate_schema_data_warehouse,
    op_kwargs=get_mssql_config(),
    dag=dag
)

fill_data_warehouse_task = PythonOperator(
    task_id='fill_data_warehouse_task',
    python_callable=None,
    op_kwargs=None,
    dag=dag
)

# Set the dependencies between the tasks.
create_data_warehouse_task >> fill_data_warehouse_task