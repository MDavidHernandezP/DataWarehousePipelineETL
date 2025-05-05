# This is an Airflow DAG that generates database schemas for different databases.
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from scripts.schemaGenerator import generate_schema_mssql, generate_schema_mysql, generate_schema_oracle, generate_schema_postgresql, generate_schema_sqlite
from config import get_mssql_config, get_mysql_config, get_oracle_config, get_postgresql_config, get_sqlite_config

dag = DAG(
    'dag_1_schema_generator',
    default_args={
        'owner': 'airflow',
        'start_date': '2025-05-01',
        'retries': 1,
    },
    schedule_interval=None,
    catchup=False
)

generate_mssql_schema_task = PythonOperator(
    task_id='generate_mssql_schema',
    python_callable=generate_schema_mssql,
    op_kwargs=get_mssql_config(),
    dag=dag
)

generate_mysql_schema_task = PythonOperator(
    task_id='generate_mysql_schema',
    python_callable=generate_schema_mysql,
    op_kwargs=get_mysql_config(),
    dag=dag
)

generate_oracle_schema_task = PythonOperator(
    task_id='generate_oracle_schema',
    python_callable=generate_schema_oracle,
    op_kwargs=get_oracle_config(),
    dag=dag
)

generate_postgresql_schema_task = PythonOperator(
    task_id='generate_postgresql_schema',
    python_callable=generate_schema_postgresql,
    op_kwargs=get_postgresql_config(),
    dag=dag
)

generate_sqlite_schema_task = PythonOperator(
    task_id='generate_sqlite_schema',
    python_callable=generate_schema_sqlite,
    op_kwargs=get_sqlite_config(),
    dag=dag
)

# Set the dependencies between the tasks.
generate_mssql_schema_task >> generate_mysql_schema_task >> generate_oracle_schema_task >> generate_postgresql_schema_task >> generate_sqlite_schema_task