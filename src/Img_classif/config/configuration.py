from Img_classif.constants import *
from Img_classif.utils.common import create_directories, read_yaml
from Img_classif.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, Model_trainer_config, Modelevaluationconfig

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
    
    def get_prepareBaseModel(self)->PrepareBaseModelConfig:
        base_model_config = PrepareBaseModelConfig(
        root_dir = self.config.base_model_prep.root_dir,
        base_model_path = self.config.base_model_prep.base_model_path,
        params_img_size = self.params.img_size,
        params_lr = self.params.lr,
        params_classes = self.params.classes)

        return base_model_config
    
    def get_trainModel(self)->Model_trainer_config:
        updated_model_config = Model_trainer_config(
        root_dir = self.config.model_trainer.root_dir,
        base_model_path = self.config.base_model_prep.base_model_path,
        updated_model_path = self.config.model_trainer.updated_model_path,
        data_path = self.config.model_trainer.data_path,
        epoch = self.params.epochs,
        batch_size = self.params.batch_size,
        img_size=self.params.img_size
        )

        return updated_model_config
    
    def get_model_eval_conf(self)->Modelevaluationconfig:
        eval_config = Modelevaluationconfig(
        model_path = self.config.model_trainer.updated_model_path,
        data_path = self.config.model_trainer.data_path,
        batch_size = self.params.batch_size,
        img_size=self.params.img_size,
        root_dir = self.config.model_evaluation.root_dir,
        eval_path = self.config.model_evaluation.eval_path,
        param_all = self.params,
        mlflow_uri = self.config.model_evaluation.mlflow_uri)
        return eval_config