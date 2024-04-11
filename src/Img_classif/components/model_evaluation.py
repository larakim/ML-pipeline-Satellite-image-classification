import tensorflow as tf
from sklearn.metrics import classification_report
import numpy as np
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from Img_classif.utils.common import create_directories, save_json
from pathlib import Path
from Img_classif.config.configuration import Modelevaluationconfig

class Model_evaluation():

    def __init__(self,config: Modelevaluationconfig) -> None:
        self.config = config
        create_directories([self.config.root_dir])

    def validation_generator(self):

        input_shape=eval(self.config.img_size)
        # Initialize the ImageDataGenerator (here, we're just rescaling the images)
        train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                fill_mode='nearest',
            validation_split=0.2) 

        self.ds_val = train_datagen.flow_from_directory(
            self.config.data_path,
            color_mode="rgb",
            batch_size=self.config.batch_size,
            shuffle=False,
            seed=10,
            subset='validation',
            interpolation="nearest",
            target_size=input_shape[:2],
        )
        self.labels = dict((v,k) for k,v in (self.ds_val.class_indices).items())
    
    def load_model(self):
        return tf.keras.models.load_model(self.config.model_path)
    
    def evaluation(self):
        
        self.model = self.load_model()
        predictions = self.model.predict(self.ds_val, verbose = 1)

        predicted_class_indices=np.argmax(predictions,axis=1)
        predictedLables= [self.labels[k] for k in predicted_class_indices]
        actualLables= [self.labels[k] for k in self.ds_val.classes]

        # Classification report
        self.cr = classification_report(actualLables, predictedLables, output_dict=True)
        dic = self.cr['weighted avg']
        dic['accuracy'] = self.cr['accuracy']
        self.save_report(dic)

    def save_report(self,dic):
        save_json(filename=Path(self.config.eval_path), data=dic)

    def log_into_mlflow(self):

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        with mlflow.start_run():
            mlflow.log_params(self.config.param_all)
            dic_score = self.cr['weighted avg']
            dic_score['accuracy'] = self.cr['accuracy']
            mlflow.log_metrics(dic_score
            )
            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.keras.log_model(self.model, "model", registered_model_name="Xception")
            else:
                mlflow.keras.log_model(self.model, "model")


    