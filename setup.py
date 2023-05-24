from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    requirements = []

    with open (file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements



setup(
    name="RegressionProject",
    version='0.0.1',
    author = 'Pranjit Chowdhury',
    author_email='pranjitchowdhury98@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages = find_packages()
)