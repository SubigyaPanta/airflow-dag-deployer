## Installation
`pip install airflow-dag-deployer`

## Deploy dags with commandline
Dags can be deployed as zip archive or independent python file prefixed by project name.

### Deploying dags as a zip archive
`python3 ../src/deploy_dag.py --project={self.project_name} --source={self.dags_dir} --destination={self.airflow_home} --method=zip`