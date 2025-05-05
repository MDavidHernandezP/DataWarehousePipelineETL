# This DAG is responsible for ingesting data to various databases.
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from scripts.dataIngestor import data_ingestor_mssql, data_ingestor_mysql, data_ingestor_oracle, data_ingestor_postgresql, data_ingestor_sqlite
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

ingest_mssql_data_task = PythonOperator(
    task_id='ingest_mssql_data',
    python_callable=data_ingestor_mssql,
    op_kwargs=get_mssql_config(),
    dag=dag
)

ingest_mysql_data_task = PythonOperator(
    task_id='ingest_mysql_data',
    python_callable=data_ingestor_mysql,
    op_kwargs=get_mysql_config(),
    dag=dag
)

ingest_oracle_data_task = PythonOperator(
    task_id='ingest_oracle_data',
    python_callable=data_ingestor_oracle,
    op_kwargs=get_oracle_config(),
    dag=dag
)

ingest_postgresql_data_task = PythonOperator(
    task_id='ingest_postgresql_data',
    python_callable=data_ingestor_postgresql,
    op_kwargs=get_postgresql_config(),
    dag=dag
)

ingest_sqlite_data_task = PythonOperator(
    task_id='ingest_sqlite_data',
    python_callable=data_ingestor_sqlite,
    op_kwargs=get_sqlite_config(),
    dag=dag
)

# Set the dependencies between the tasks.
ingest_mssql_data_task >> ingest_mysql_data_task >> ingest_oracle_data_task >> ingest_postgresql_data_task >> ingest_sqlite_data_task