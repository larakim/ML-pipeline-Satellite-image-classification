import tensorflow as tf
from img_classif import logger
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau # type: ignore
from sklearn.metrics import confusion_matrix, average_precision_score, recall_score, precision_score, accuracy_score, classification_report
from img_classif.config.configuration import Model_trainer_config
from img_classif.utils.common import read_yaml, create_directories
from img_classif.constants import *

class Modeltrainer:
    def __init__(self, config: Model_trainer_config):
        self.config = config
        create_directories([self.config.root_dir])

    def train_model(self):
        """
        """
        # Loading model
        base_model = tf.keras.models.load_model(self.config.base_model_path)
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

        ds_train = train_datagen.flow_from_directory(
            self.config.data_path,
            color_mode="rgb",
            batch_size=self.config.batch_size,
            shuffle=False,
            seed=10,
            subset='training',
            interpolation="nearest",
            target_size=input_shape[:2],
        )
        ds_val = train_datagen.flow_from_directory(
            self.config.data_path,
            color_mode="rgb",
            batch_size=self.config.batch_size,
            shuffle=False,
            seed=10,
            subset='validation',
            interpolation="nearest",
            target_size=input_shape[:2],
        )
        labels = dict((v,k) for k,v in (ds_val.class_indices).items())

        logger.info('In train_generator')
        for i in range(len (ds_train.class_indices)):
            print(labels[i],":\t",list(ds_train.classes).count(i))
   

        logger.info('In validation_generator')
        for i in range(len (ds_val.class_indices)):
            print(labels[i],":\t",list(ds_val.classes).count(i))

    
        # Define callbacks
        checkpoint = ModelCheckpoint(self.config.updated_model_path, verbose=1, monitor='val_loss', save_best_only=True, mode='auto')

        # EarlyStopping to stop training when the validation loss has not improved after 5 epochs
        early_stopping = EarlyStopping(monitor='val_loss', patience=5, verbose=1, mode='auto')

        # ReduceLROnPlateau to reduce the learning rate when the validation loss has stopped improving
        reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, verbose=1, mode='auto', min_lr=0.00001)

        # Start model training
        ds_train.reset()
        ds_val.reset()

        # Fit the model
        history = base_model.fit(
            ds_train,
            epochs=self.config.epoch,  # Adjust based on your needs
            validation_data=ds_val,
            callbacks=[checkpoint, early_stopping, reduce_lr]
        )
        logger.info('Saving trained model')
        # base_model.save(self.config.updated_model_path)
        logger.info(f'Trained model saved at {self.config.updated_model_path}')
