
from img_classif.config.configuration import ConfigurationManager
from img_classif import logger
from img_classif.components.model_evaluation import Model_evaluation


STAGE_NAME = 'Model evaluation stage'


class Modelevaluationpipeline():
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        config_eval = config.get_model_eval_conf()
        eval_model = Model_evaluation(config=config_eval)
        eval_model.validation_generator()
        eval_model.evaluation()
        eval_model.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f'Stage {STAGE_NAME} started')
        obj = Modelevaluationpipeline()
        obj.main()
        logger.info(f'Stage {STAGE_NAME} done successfully \n')
    except Exception as e:
        logger.exception(e)
        raise e