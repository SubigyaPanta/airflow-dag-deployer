from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.docker.operators.docker import DockerOperator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'Test',
    default_args=default_args,
    description='First test Deepboard Dag',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['test_dag'],
)

t1 = DockerOperator(image='test_image/test-workflow:0.2',
                    command='python application.py extract',
                    task_id='extract',
                    dag=dag,
                    # docker_url='tcp://host.docker.internal:2375',
                    docker_url="unix://var/run/docker.sock",
                    network_mode='bridge')

t2 = DockerOperator(image='test_image/test-workflow:0.2',
                    command='python application.py load',
                    task_id='load',
                    depends_on_past=False,
                    dag=dag,
                    docker_url="unix://var/run/docker.sock",
                    network_mode='bridge')


t3 = DockerOperator(image='test_image/test-workflow:0.2',
                    command='python application.py transform',
                    task_id='transform',
                    depends_on_past=False,
                    dag=dag,
                    docker_url="unix://var/run/docker.sock",
                    network_mode='bridge')

t1 >> t2 >> t3
