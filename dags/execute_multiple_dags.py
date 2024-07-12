from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.bash import BashOperator

default_args= {
    'owner' : 'hadoop',
}

with DAG(
    dag_id = 'executing_multiple_dags',
    description = 'Dags with multiple excutioner',
    default_args= default_args,
    start_date= days_ago(1),
    schedule_interval='@once'
) as dag1:

    taskA = BashOperator(

        task_id = 'taskA',
        bash_command= 'echo TaskA Executed'
    )

    taskB = BashOperator(

        task_id = 'taskB',
        bash_command= 'echo TaskB Executed'
    )

taskA.set_downstream(taskB)