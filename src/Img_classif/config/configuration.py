from img_classif.constants import *
from img_classif.utils.common import create_directories, read_yaml
from img_classif.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_path = CONFIG_FILE_PATH,param_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(param_path)

    def get_data_ingestion_config(self)->DataIngestionConfig:
        data_ing_config = DataIngestionConfig(
        source_url = self.config.data_ingestion.source_url,
        root_dir = self.config.data_ingestion.root_dir,
        zip_file = self.config.data_ingestion.zip_file)

        return data_ing_config
