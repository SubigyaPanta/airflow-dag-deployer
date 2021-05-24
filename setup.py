import setuptools

with open('README.md', 'r') as handle:
    long_description = handle.read()

setuptools.setup(
    name='airflow-dag-deployer',
    version='0.5',
    author='Subigya Jyoti Panta',
    author_email='subigyapanta@gmail.com',
    description="To deploy projects dags to airflow dag directory",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/SubigyaPanta/airflow-dag-deployer.git",
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires=">=3.7",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    project_urls={
            'Bug Reports': 'https://github.com/SubigyaPanta/airflow-dag-deployer/issues',
            'Source': 'https://github.com/SubigyaPanta/airflow-dag-deployer.git',
        },
    entry_points = {
        'console_scripts': [
            'deploydag = dagdeployer.deploy_dag:run',
        ],
    }
)
