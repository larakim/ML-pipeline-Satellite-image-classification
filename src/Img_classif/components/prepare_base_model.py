import keras
from img_classif.config.configuration import PrepareBaseModelConfig
from img_classif import logger
from img_classif.utils.common import create_directories

class PrepareBaseModel:

    def __init__(self,config:PrepareBaseModelConfig):
        self.config = config
        create_directories([self.config.root_dir])

    def get_base_model(self):
        self.model = keras.applications.Xception(
            weights="imagenet",  # Load weights pre-trained on ImageNet.
            input_shape=eval(self.config.params_img_size),
            include_top=False,
        )

    def update_base_model(self):
        self.model.trainable = False
        # Create new model on top
        inputs = keras.Input(shape=eval(self.config.params_img_size))

        # Pre-trained Xception weights requires that input be scaled
        # from (0, 255) to a range of (-1., +1.), the rescaling layer
        # outputs: `(inputs * scale) + offset`
        scale_layer = keras.layers.Rescaling(scale=1 / 127.5, offset=-1)
        x = scale_layer(inputs)

        x = self.model(x,training=False)  
        x = keras.layers.GlobalAveragePooling2D()(x)
        x = keras.layers.Dropout(0.2)(x)  # Regularize with dropout
        predictions = keras.layers.Dense(self.config.params_classes,activation='softmax')(x)

        # Create the model
        full_model = keras.Model(inputs,predictions)

        # Print the model summary
        full_model.summary()

        full_model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=self.config.params_lr),
            loss='categorical_crossentropy',
            metrics=['accuracy'],
            )

        full_model.save(self.config.base_model_path)
        logger.info(f'Base model successfully saved at {self.config.base_model_path}')