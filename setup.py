from setuptools import find_packages,setup
from typing import List

HYPHER_E_DOT = '-e .'

def get_requirements(filepath:str)->List[str]:

    requirements=[]

    with open(filepath) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPHER_E_DOT in requirements:
            requirements.remove(HYPHER_E_DOT)



setup(
    name="MLproject",
    version="0.0.1",
    author="Gaurav",
    author_eamil="gramoliya39@gamil.com",
    install_requires =get_requirements('requirements.txt'),
    get_packages=find_packages()
)