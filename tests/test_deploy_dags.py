import unittest
import os
import glob
from src.deploy_dag import Deployer


class DeployTest(unittest.TestCase):

    def setUp(self) -> None:
        self.airflow_home = 'airflowhome'
        self.dags_dir = 'dags'
        self.project_name = 'deepboard'

        # clear everything in airflow home directory
        # files = glob.glob(self.airflow_home)
        # for f in files:
        #     os.remove(f)

    def test_files_deploy(self):
        deployer = Deployer(self.project_name, self.dags_dir, self.airflow_home, 'file')
        deployer.run()

        file_to_check = f'{self.airflow_home}/{self.project_name}_testetl.py'
        exists = os.path.isfile(file_to_check)
        self.assertTrue(exists)

        os.remove(file_to_check)

    def test_zip_deploy(self):
        deployer = Deployer(self.project_name, self.dags_dir, self.airflow_home, 'zip')
        deployer.run()

        file_to_check = f'{self.airflow_home}/{self.project_name}.zip'
        exists = os.path.isfile(file_to_check)
        self.assertTrue(exists)

        os.remove(file_to_check)

    def test_zip_deploy_commandline(self):
        os.system(f'python3 ../src/deploy_dag.py --project={self.project_name} --source={self.dags_dir} --destination={self.airflow_home} --method=zip')

        file_to_check = f'{self.airflow_home}/{self.project_name}.zip'
        exists = os.path.isfile(file_to_check)
        self.assertTrue(exists)

        os.remove(file_to_check)
