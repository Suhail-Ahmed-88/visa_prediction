from setuptools import find_packages, setup
from typing import List


# HYFEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requiremnts
    '''
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]
        
        
        # if HYFEN_E_DOT in requirements:
        #     requirements.remove(HYFEN_E_DOT)
        
    return requirements
        


setup(
    project_name = "College Student Project",
    version="0.0.1",
    author="Suhail Ahmed",
    author_email="rajpar.suhail.ahmed@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
    
)