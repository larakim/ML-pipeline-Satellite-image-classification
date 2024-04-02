
from img_classif.components.data_ingestion import DataIngestion
from img_classif.config.configuration import ConfigurationManager
from img_classif import logger


STAGE_NAME = 'Data ingestion stage'


class Dataingestionpipeline():
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_config = config.get_data_ingestion_config()
        data_ingestion_i = DataIngestion(data_config)
        data_ingestion_i.download_data()
        data_ingestion_i.unzip_data()

if __name__ == '__main__':
    try:
        logger.info(f'Stage {STAGE_NAME} started')
        obj = Dataingestionpipeline()
        obj.main()
        logger.info(f'Stage {STAGE_NAME} done successfully \n')
    except Exception as e:
        logger.exception(e)
        raise e