"""A liveness prober dag for monitoring composer.googleapis.com/environment/healthy."""
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator
from datetime import timedelta, datetime

default_args = {
    'owner' : 'airflow',
    'start_date': datetime(2024, 7, 24),
    'depends_on_past' : False,
    'email': ['raghavendra369@gmail.com'],
    'email_on_failure': False,
    'email_on_retry' : False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'fetch_cricket_stats',
    default_args=default_args,
    description='runs an external python script for extracting data',
    schedule_interval='@daily',
    catchup=False
)

# priority_weight has type int in Airflow DB, uses the maximum.

with dag:
    run_script_task = BashOperator(
        task_id='run_script',
        bash_command='python /home/airflow/gcs/dags/scripts/cricket_ranking.py'
    )
