from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from callables.data_engineering_callable import data_engineering
from callables.model_engineering_callable import model_engineering
from callables.start_services_callable import start_services_callable


#Define default arguments
default_args = {
 'owner': 'your_name',
 'start_date': datetime(2024, 10, 1),
 'retries': 1,
}

# Instantiate your DAG
dag = DAG(
    'model_train',
    default_args=default_args,
    schedule_interval='*/5 * * * *',
    catchup=False,
)


data_engineering_task = PythonOperator(
    task_id='data_engineering_task',
    python_callable=data_engineering,
    dag=dag,
)


model_engineering_task = PythonOperator(
    task_id='model_engineering_task',
    python_callable=model_engineering,
    dag=dag,
)


start_services_task = PythonOperator(
    task_id='start_services_task',
    python_callable=start_services_callable,
    dag=dag,
)


data_engineering_task >> model_engineering_task >> start_services_task
