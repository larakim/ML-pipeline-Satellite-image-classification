
from Img_classif.config.configuration import ConfigurationManager
from Img_classif import logger
from Img_classif.components.prepare_base_model import PrepareBaseModel


STAGE_NAME = 'Base model preparation stage'


class BaseModelpipeline():
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_prepareBaseModel()
        base_model_c = PrepareBaseModel(base_model_config)
        base_model_c.get_base_model()
        base_model_c.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f'Stage {STAGE_NAME} started')
        obj = BaseModelpipeline()
        obj.main()
        logger.info(f'Stage {STAGE_NAME} done successfully \n')
    except Exception as e:
        logger.exception(e)
        raise e