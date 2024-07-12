from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.bash import BashOperator

default_args= {
    'owner' : 'hadoop',
}

with DAG(
    dag_id = 'hello_world',
    description = 'our First Hello World DAG:',
    default_args= default_args,
    start_date= days_ago(1),
    schedule_interval='@daily',
    tags = ['beginner','bash','hello_world']
) as dag:

    task = BashOperator(

        task_id = 'hello_world_task_id',
        bash_command= 'echo Hello World again',
        dag = dag
    )

task