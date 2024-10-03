FROM apache/airflow:2.9.2-python3.12

ENV AIRFLOW_HOME=/opt/airflow

WORKDIR /opt/airflow

COPY requirements.txt .
RUN pip install -r requirements.txt
