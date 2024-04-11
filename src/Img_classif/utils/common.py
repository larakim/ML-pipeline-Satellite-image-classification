import os
import json
from ensure import ensure_annotations
import yaml
from pathlib import Path
import joblib
from Img_classif import logger
from box.exceptions import BoxValueError
from box import ConfigBox
import base64

@ensure_annotations
def read_yaml(filename:Path)->ConfigBox:
    """
    Read yaml file

    Args:
        filename (str): Path of the yaml file
    Raises:
        Error: if empty file or uncorrect format
    return:
        ConfigBox: yaml file content converted to ConfigBox type
    """

    try:
        with open(filename) as f:
            yaml_content = yaml.safe_load(f)
            logger.info(f'{filename} loaded successfully')
        return ConfigBox(yaml_content)
    except BoxValueError:
        raise ValueError('YAML file is empty')
    except Exception as e:
        raise e

@ensure_annotations
def read_json(filename:Path)->ConfigBox:
    """
    Read Json file

    Args: 
        filename (str): Json file path
    Raises: 
        Exception: If uncorrect format
    return:
        ConfigBox: Json file content as ConfigBox type
    """
    try:
        with open(filename,'r') as f:
            json_content = json.load(filename)
            logger.info(f'{filename} loaded successfully')
            return ConfigBox(json_content)
        
    except Exception as e:
        raise e

@ensure_annotations
def save_json(filename: Path, data: dict):
    """
    Save data in Json file
    Args:
        filename (str): Path of the json file
        data (dict): Data to be saved
    Raises:
        Exception: If uncorrect data
    """

    try: 
        with open(filename,'w') as f:
            json.dump(data,f)
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    
