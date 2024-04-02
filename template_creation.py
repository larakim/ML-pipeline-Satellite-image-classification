import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format= '%(asctime)s : %(message)s')

project_name = 'Img_classif'

files_path = [
            '.github/workflows/.gitkeep',
            'dvc.yaml',
            'requirements.txt',
            'setup.py',
            'config/config.yaml',
            'templates/index.html',
            'params.yaml',
            f'src/{project_name}/__init__.py',
            f'src/{project_name}/components/__init__.py',
            f'src/{project_name}/utils/__init__.py',
            f'src/{project_name}/pipeline/__init__.py',
            f'src/{project_name}/config/__init__.py',
            f'src/{project_name}/config/configuration.py',
            f'src/{project_name}/entity/__init__.py',
            f'src/{project_name}/constants/__init__.py',
            f'research/test.ipynb',
]


for file in files_path:
    file = Path(file)
    filedir,filepath = os.path.split(file)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating file directory {filedir} ')

    if (not os.path.exists(file)):
        with open(file,'w') as f:
            pass
        logging.info(f'Creating file {file}')
    else:
        logging.info(f'{file} already exists')
    
