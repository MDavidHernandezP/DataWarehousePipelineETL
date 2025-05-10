# Data warehouse gold layer creation DAG by transforming the bronze layer with Data Build Tool.
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

dag = DAG(
    'dag_5_dbt_manager',
    default_args={
        'owner': 'airflow',
        'start_date': '2025-05-01',
        'retries': 1,
    },
    schedule_interval=None,
    catchup=False
)
