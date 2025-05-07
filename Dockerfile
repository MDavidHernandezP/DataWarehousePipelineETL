FROM apache/airflow:2.7.1-python3.9

USER root
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copiar todos los archivos del proyecto
COPY . /opt/airflow/

# Ajustar permisos si es necesario
RUN chown -R airflow: /opt/airflow

USER airflow