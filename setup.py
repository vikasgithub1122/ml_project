from setuptools import find_packages, setup
from typing import List

Hyphen_e_Dot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this fun will return requirements,txt
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hyphen_e_Dot in requirements:
            requirements.remove(Hyphen_e_Dot)
    return requirements
setup(
name='machine learning project',
version='0.01',
author='Vikas',
author_email='jaihind9306908@gmail.com',
package=find_packages(),
install_requires=get_requirements('requirement.txt')

)