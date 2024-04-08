from img_classif.pipeline.stage_01_data_ingestion import Dataingestionpipeline
from img_classif.pipeline.stage_02_prepare_base_model import BaseModelpipeline
from img_classif.pipeline.stage_03_model_trainer import Modeltrainerpipeline
from img_classif.pipeline.stage_04_model_evaluation import Modelevaluationpipeline
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
    

STAGE_NAME = 'Base model preparation stage'

if __name__ == '__main__':
    try:
        logger.info(f'Stage {STAGE_NAME} started')
        obj = BaseModelpipeline()
        obj.main()
        logger.info(f'Stage {STAGE_NAME} done successfully \n')
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = 'Model training stage'

if __name__ == '__main__':
    try:
        logger.info(f'Stage {STAGE_NAME} started')
        obj = Modeltrainerpipeline()
        obj.main()
        logger.info(f'Stage {STAGE_NAME} done successfully \n')
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = 'Model Evaluation stage'

if __name__ == '__main__':
    try:
        logger.info(f'Stage {STAGE_NAME} started')
        obj = Modelevaluationpipeline()
        obj.main()
        logger.info(f'Stage {STAGE_NAME} done successfully \n')
    except Exception as e:
        logger.exception(e)
        raise e