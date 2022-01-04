from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import pickle
import cv2
import os

####################### our custom model class #################################

class ActivityModel:
    # initialise the model layers
    def __init__(batch_size=32):
        baseModel = ResNet50(weights="imagenet",                                        # Loading the ResNet 50 Network
            include_top=False,						                                    # Ensuring the head FC layers are left off
        	input_tensor=Input(shape=(224, 224, 3)))									# Our input shape is 224 * 224, images will resized to this size

        headModel = baseModel.output													# Constructing the head of the model that will be placed on top of the base model
        headModel = AveragePooling2D(pool_size=(7, 7))(headModel)                       # Average pooling layers
        headModel = Flatten(name="flatten")(headModel)                                  # Flatten layer
        headModel = Dense(512, activation="relu")(headModel)                            # Dense or fully connected layer, with relu as activation
        headModel = Dropout(0.5)(headModel)                                             # Dropout rate of 0.5
        headModel = Dense(len(lb.classes_), activation="softmax")(headModel)            # Final softmax layer for class predictions

        self.model = Model(inputs=baseModel.input, outputs=headModel)					# Placing the head FC model on top of base model (This is the actual model that we'll train)

        for layer in baseModel.layers:													# Looping over all layers in base model and freezing them so they won't be trained during training process
            layer.trainable = False                                                     # As we want to use the ResNet weights

        self.batch_size = 32

    # load the images and labels and fit to appropriate data type
    def loadData(LABELS, imagePaths):
        self.data = []																    # Array to store the loaded images
        self.labels = []															    # Array to store the labels

        for imagePath in imagePaths:													# Iterating over each image path
        	label = imagePath.split(os.path.sep)[-2]									# Extracting the labels from the filename
        	if label not in LABELS:														# If image doesn't belong to any defined label then ignore the image
        		continue

        	image = cv2.imread(imagePath)												# Reading the image
        	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)								# Converting all the images to RGB Channel
        	image = cv2.resize(image, (224, 224))										# Downsizing (Resizing) the images to the same resolution for symmetry and faster training
        	self.data.append(image)														# Update the data array accordingly
        	self.labels.append(label)													# Update the labels array accordingly

        self.data = np.array(self.data)													# Converting data into numpy array
        self.labels = np.array(self.labels)												# Converting labels into numpy array

        self.lb = LabelBinarizer()														# Performing one-hot encoding on the labels
        self.labels = lb.fit_transform(self.labels)

    def saveLabels(path):
        f = open(path, "wb")												            # Serializing the labels to disk
        f.write(pickle.dumps(self.lb))
        f.close()

    # split data into train/test and set the augmentations to be applied
    def splitAugmentData(zoom=0.15, hflip=True):
        (self.trainX, self.testX, self.trainY, self.testY) = train_test_split(
            self.data, self.labels,	                                                    # Dividing the data into train and validation (75% train and 25% validation by default)
        	test_size=0.25, stratify=labels, random_state=42)

        self.trainGen = ImageDataGenerator(												# Applying augmentations (horizontal_flip & slight zoom)
        	zoom_range=zoom,
        	horizontal_flip=hflip
        )

        self.valGen = ImageDataGenerator()												# No augmentation for validation as we want to test the original data

        mean = np.array([123.68, 116.779, 103.939], dtype="float32")					# Defining ImageNetmean subtraction(in RGB order) & setting subtraction value for each object
        self.trainAug.mean = mean
        self.alAug.mean = mean

        return self.trainX, self.testX, self.trainY, self.testY

    # set training parameters and compile model
    def compile(_lr=1e-4, _momentum=0.9, _decay=1e-4, epochs):							# Compiling our model (Done once all layers are set to be non-trainable)
        opt = SGD(lr=_lr, momentum=_momentum, decay=_decay / epochs)                    # Setting the optimiser

        self.model.compile(loss="binary_crossentropy", optimizer=opt,				    # Using binary_crossentropy for two classes (we have a true class and a false class)
        	metrics=["accuracy"])

    # train the model
    def fit(_epochs):
        self.history = self.model.fit(																	# This will allow the new FC layers to be initialized with actual learned values instead of random ones
        	x=self.trainAug.flow(self.trainX, self.trainY, batch_size=self.batch_size),
        	steps_per_epoch=len(self.trainX) // 32,
        	validation_data=self.valAug.flow(self.testX, self.testY),
        	validation_steps=len(self.testX) // 32,
        	epochs=_epochs)

    def saveTrainingPlot(_epochs, save_path):
        N = _epochs																# Plotting the training loss and accuracy
        plt.style.use("ggplot")
        plt.figure()
        plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
        plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
        plt.plot(np.arange(0, N), H.history["accuracy"], label="train_acc")
        plt.plot(np.arange(0, N), H.history["val_accuracy"], label="val_acc")
        plt.title("Training Loss and Accuracy on Dataset")
        plt.xlabel("Epoch #")
        plt.ylabel("Loss/Accuracy")
        plt.legend(loc="lower left")
        plt.savefig(save_path)

    def predict(testX):
        self.model.predict(x=testX.astype("float32"), batch_size=self.batch_size)

    def save(path, format):
        model.save(path, save_format=format)
