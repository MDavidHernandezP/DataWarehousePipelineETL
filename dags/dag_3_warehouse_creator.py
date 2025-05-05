# Data warehouse creation DAG with Specific operator from Airflow.
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from scripts.dataWarehouse import generate_schema_data_warehouse, load_tables_data_warehouse
from scripts.tableExtractor import table_extractor_mssql, table_extractor_mysql, table_extractor_oracle, table_extractor_postgresql, table_extractor_sqlite
from config import get_data_warehouse_config, get_mssql_config, get_mysql_config, get_oracle_config, get_postgresql_config, get_sqlite_config

def load_mssql_to_data_warehouse():
    mssql_cfg = get_mssql_config()
    
    data_warehouse_cfg = get_data_warehouse_config()

    mssql_df = table_extractor_mssql(**mssql_cfg, table_name="purchases")

    load_tables_data_warehouse(**data_warehouse_cfg, table_name="purchases", schema_name="bronze", df=mssql_df)

def load_mysql_to_data_warehouse():
    mysql_cfg = get_mysql_config()

    data_warehouse_cfg = get_data_warehouse_config()

    mysql_df = table_extractor_mysql(**mysql_cfg, table_name="products")

    load_tables_data_warehouse(**data_warehouse_cfg, table_name="products", schema_name="bronze", df=mysql_df)

def load_oracle_to_data_warehouse():
    oracle_cfg = get_oracle_config()

    data_warehouse_cfg = get_data_warehouse_config()

    oracle_df = table_extractor_oracle(**oracle_cfg, table_name="checkout")

    load_tables_data_warehouse(**data_warehouse_cfg, table_name="checkout", schema_name="bronze", df=oracle_df)

def load_postgresql_to_data_warehouse():
    postgresql_cfg = get_postgresql_config()

    data_warehouse_cfg = get_data_warehouse_config()

    postgresql_df = table_extractor_postgresql(**postgresql_cfg, table_name="sales")

    load_tables_data_warehouse(**data_warehouse_cfg, table_name="sales", schema_name="bronze", df=postgresql_df)

def load_sqlite_to_data_warehouse():
    sqlite_cfg = get_sqlite_config()

    data_warehouse_cfg = get_data_warehouse_config()

    sqlite_df = table_extractor_sqlite(**sqlite_cfg, table_name="employees")

    load_tables_data_warehouse(**data_warehouse_cfg, table_name="employees", schema_name="bronze", df=sqlite_df)

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
    python_callable=load_mssql_to_data_warehouse,
    dag=dag
)

fill_2_data_warehouse_task = PythonOperator(
    task_id='fill_2_data_warehouse_task',
    python_callable=load_mysql_to_data_warehouse,
    dag=dag
)

fill_3_data_warehouse_task = PythonOperator(
    task_id='fill_3_data_warehouse_task',
    python_callable=load_oracle_to_data_warehouse,
    dag=dag
)

fill_4_data_warehouse_task = PythonOperator(
    task_id='fill_4_data_warehouse_task',
    python_callable=load_postgresql_to_data_warehouse,
    dag=dag
)

fill_5_data_warehouse_task = PythonOperator(
    task_id='fill_5_data_warehouse_task',
    python_callable=load_sqlite_to_data_warehouse,
    dag=dag
)

# Set the dependencies between the tasks.
create_data_warehouse_task >> fill_1_data_warehouse_task >> fill_2_data_warehouse_task >> fill_3_data_warehouse_task >> fill_4_data_warehouse_task >> fill_5_data_warehouse_task