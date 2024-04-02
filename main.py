from img_classif.pipeline.stage_01_data_ingestion import Dataingestionpipeline
from img_classif import logger




STAGE_NAME = 'Data ingestion stage'



if __name__ == '__main__':
    try:
        logger.info(f'Stage {STAGE_NAME} started')
        obj = Dataingestionpipeline()
        obj.main()
        logger.info(f'Stage {STAGE_NAME} done successfully \n')
    except Exception as e:
        logger.exception(e)
        raise e