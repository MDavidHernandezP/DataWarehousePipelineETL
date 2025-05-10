# Data warehouse silver layer creation DAG by transforming the bronze layer with Great Expectations.
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

dag = DAG(
    'dag_4_great_expectations',
    default_args={
        'owner': 'airflow',
        'start_date': '2025-05-01',
        'retries': 1,
    },
    schedule_interval=None,
    catchup=False
)
