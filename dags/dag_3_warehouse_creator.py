# Data warehouse creation DAG with Specific operator from Airflow.
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from scripts.dataWarehouse import generate_schema_data_warehouse, load_mssql_tables, load_mysql_tables, load_oracle_tables, load_postgresql_tables, load_sqlite_tables
from config import get_mssql_config, get_mysql_config, get_oracle_config, get_postgresql_config, get_sqlite_config

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

fill_1_data_warehouse_task = PythonOperator(
    task_id='fill_1_data_warehouse_task',
    python_callable=load_mssql_tables,
    op_kwargs={
        **get_mssql_config(),
        "table_name": "your_table_name_here"
    },
    dag=dag
)

fill_2_data_warehouse_task = PythonOperator(
    task_id='fill_2_data_warehouse_task',
    python_callable=load_mysql_tables,
    op_kwargs={
        **get_mysql_config(),
        "table_name": "your_table_name_here"
    },
    dag=dag
)

fill_3_data_warehouse_task = PythonOperator(
    task_id='fill_3_data_warehouse_task',
    python_callable=load_oracle_tables,
    op_kwargs={
        **get_oracle_config(),
        "table_name": "your_table_name_here"
    },
    dag=dag
)

fill_4_data_warehouse_task = PythonOperator(
    task_id='fill_4_data_warehouse_task',
    python_callable=load_postgresql_tables,
    op_kwargs={
        **get_postgresql_config(),
        "table_name": "your_table_name_here"
    },
    dag=dag
)

fill_5_data_warehouse_task = PythonOperator(
    task_id='fill_5_data_warehouse_task',
    python_callable=load_sqlite_tables,
    op_kwargs={
        **get_sqlite_config(),
        "table_name": "your_table_name_here"
    },
    dag=dag
)

# Set the dependencies between the tasks.
create_data_warehouse_task >> fill_1_data_warehouse_task >> fill_2_data_warehouse_task >> fill_3_data_warehouse_task >> fill_4_data_warehouse_task >> fill_5_data_warehouse_task