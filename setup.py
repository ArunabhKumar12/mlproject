from setuptools import find_packages, setup 
from typing import List 

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    # This fn will return a list 
    '''
    this function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Below code is to remove the \n which is being read along with the lines in txt file
        requirements = [req.replace("\n", "") for req in requirements]

        # -e . mentioned in the requirements file will automatically trigger this file to run while running the project. So we need to prevent it to be read as a requirement

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements 

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Arunabh',
    author_email = 'arunabhkumar2002@gmail.com',
    packages = find_packages(),
    install_requires = ['pandas', 'numpy', 'seaborn']
)