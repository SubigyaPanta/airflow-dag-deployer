## Installation
`pip install airflow-dag-deployer`

## Deploy dags with commandline
Dags can be deployed as zip archive or independent python file prefixed by project name.

### Deploying dags as a zip archive
```
deploydag --project=<project_name> --source=<dags_dir> --destination=<airflow_home> --method=zip
```

### Deploying dags as a file
```
deploydag --project=<project_name> --source=<dags_dir> --destination=<airflow_home> --method=file
```
