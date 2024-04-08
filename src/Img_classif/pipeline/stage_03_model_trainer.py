
from img_classif.config.configuration import ConfigurationManager
from img_classif import logger
from img_classif.components.model_trainer import Modeltrainer


STAGE_NAME = 'Model training stage'


class Modeltrainerpipeline():
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_trainModel()
        model_c = Modeltrainer(config=training_config)
        model_c.train_model()


if __name__ == '__main__':
    try:
        logger.info(f'Stage {STAGE_NAME} started')
        obj = Modeltrainerpipeline()
        obj.main()
        logger.info(f'Stage {STAGE_NAME} done successfully \n')
    except Exception as e:
        logger.exception(e)
        raise e