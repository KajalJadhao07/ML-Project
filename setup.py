from setuptools import find_packages, setup
from typing import List

hyphen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements'''
    requirements= []
    with open('requirements.txt') as obj:
        requirements=obj.readlines()
        [req.replace("\n", " ")for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)



setup(
    name='mlproject',
    version='0.0.1',
    author='Kajal',
    author_email='kajaljadhao16@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)