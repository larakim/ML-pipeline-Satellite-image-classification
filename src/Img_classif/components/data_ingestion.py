
import gdown
from img_classif import logger
import zipfile
import os
from img_classif.utils.common import create_directories, read_yaml
from img_classif.config.configuration import DataIngestionConfig

class DataIngestion:
    def __init__(self,data_config:DataIngestionConfig):
        self.data_config = data_config


    def download_data(self):
        '''
        Dowloading Satellite image data
        '''
        create_directories([self.data_config.root_dir])
        try:

            gdown.download(self.data_config.source_url,self.data_config.zip_file)

            logger.info(f'Data downloaded successfully')
        except Exception as e:
            raise e
    
    def unzip_data(self):

        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.data_config.root_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.data_config.zip_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(f'Data unzipped successfully')
        
    