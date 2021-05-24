import os
import shutil
import argparse
import json


class Deployer:
    """
    Deploys dags from deg directory to a packaged dag in airflow dag folder with
    a command line interface.
    """
    def __init__(self, project_name , source_dags_dir, airflow_dag_dir, deploy_method):
        """
        :param project_dag_dir: Project's Dag Directory
        :param airflow_dag_dir: Airflow's Dag Directory
        """
        self.project_name = project_name
        self.source_dags_dir = source_dags_dir
        self.airflow_dags_dir = airflow_dag_dir
        self.deploy_method = deploy_method

    def run(self):
        """
        Deploys dags
        :return:
        """
        assert self.source_dags_dir is not None, 'Source dags directory cannot be empty'
        assert self.airflow_dags_dir is not None, 'Destination dags directory (Airflow dags dir) cannot be empty'
        assert self.project_name is not None, 'Project Name cannot be empty'
        assert self.deploy_method is not None, 'Deploy method cannot be empty'

        if self.deploy_method == 'zip':
            self._deploy_zip()
        elif self.deploy_method == 'file':
            self._deploy_file()
        else:
            raise ValueError('Deploy method can be either "zip" or "file"')

    def _deploy_zip(self):
        # output_filename, type, src_dag_folder
        shutil.make_archive(self.project_name, 'zip', self.source_dags_dir)
        archive_name = f'{self.project_name}.zip'
        shutil.move(archive_name, os.path.join(self.airflow_dags_dir, archive_name))

    def _deploy_file(self):
        src_files = os.listdir(self.source_dags_dir)
        full_src_file = [os.path.join(self.source_dags_dir, sf) for sf in src_files if sf != '__init__.py']
        full_dest_file = [os.path.join(self.airflow_dags_dir, f'{self.project_name}_{sf}') for sf in src_files if sf != '__init__.py']

        for (src, dest) in zip(full_src_file, full_dest_file):
            shutil.copy(src, dest)


def run():
    parser = argparse.ArgumentParser(description="Deploys dags from deg directory to a packaged dag in "
                                                 "airflow dag folder with a command line interface.")
    parser.add_argument('--project', type=str, help="Project name to keep inside airflow dag directory")
    parser.add_argument('--source', type=str, help="Source folder for dags")
    parser.add_argument('--destination', type=str, help="Airflow dags directory")
    parser.add_argument('--method', type=str, default='file',
                        help="Deploy zip or files prefixed with project name. It takes values 'zip' or 'file'.")
    parser.add_argument('--config', type=str, default="deploydag.json",
                        help='Path of config file containing project details')
    parser.add_argument('--env', type=str, default="dev",
                        help='Environment setting for dev/test/production inside config.')

    options = parser.parse_args()

    try:

        # if config is provided
        if os.path.isfile(options.config):
            assert options.env is not None, "Env is required when you provide config"
            with open(options.config, 'r') as handle:
                cfg = json.load(handle)
            env = options.env
            project = cfg[env].get('project')
            source = cfg[env].get('source')
            destination = cfg[env].get('destination')
            method = cfg[env].get('method')
        else:
            # arguments should be passed directly
            project = options.project
            source = options.source
            destination = options.destination
            method = options.method

        deployer = Deployer(project, source, destination, method)
        deployer.run()
    except AssertionError as ae:
        print(str(ae))
    except ValueError as ve:
        print(str(ve))


if __name__ == '__main__':
    run()
