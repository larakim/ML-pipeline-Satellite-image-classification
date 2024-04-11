from img_classif.utils.common import read_yaml
from img_classif.constants import *
from img_classif.components.model_evaluation import Model_evaluation
from img_classif.config.configuration import ConfigurationManager
import keras
import numpy as np

class Image_label_prediction():

    def __ini__(self):
        pass

    def load_model_labels(self):

        config = ConfigurationManager()
        config_eval = config.get_model_eval_conf()
        eval_model = Model_evaluation(config=config_eval)
        eval_model.validation_generator()
        self.model = eval_model.load_model()
        self.labels = eval_model.labels
        self.img_size = eval_model.config.img_size

    def predict(self,img_path)->int:
        """
        Predict a label for a specific image

        Args:
            img_path (Path): Path of the image 

        return:
            predicted_class (int): Label of the input image
        """
        input_shape=eval(self.img_size)

        image = keras.utils.load_img(img_path,interpolation="nearest",
            target_size=input_shape[:2])
        input_arr = keras.utils.img_to_array(image)

        predicted_class = self.labels[np.argmax(self.model.predict(input_arr.reshape(tuple(list([1]) + list(input_shape)))))]
        proba = self.model.predict_on_batch(input_arr.reshape(tuple(list([1]) + list(input_shape))))
        return predicted_class,100*np.max(proba)
    
if __name__ == '__main__':
    img_path = 'artifacts/data_ingestion/data/desert/desert(8).jpg'
    model = Image_label_prediction()
    model.load_model_labels()
    predicted_label,proba = model.predict(img_path)
    print(predicted_label + ' probability' + str(np.round(proba*100)))