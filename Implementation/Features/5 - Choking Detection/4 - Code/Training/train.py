############################# Necessary Utilities #############################

import matplotlib																# Importing this library to display performance graphs
matplotlib.use("Agg")

import model

###############################################################################

ap = argparse.ArgumentParser()													# Designing some arguments
ap.add_argument("-d", "--dataset", required=True,								# Path to dataset
	help="Path to your dataset")
ap.add_argument("-m", "--model", required=True,									# Path & Name to save the trained model
	help="Specify the name and location of the trained model")
ap.add_argument("-l", "--label-bin", required=True,								# Path and Name of the generated labels
	help="Path of the labels generated")
ap.add_argument("-e", "--epochs", type=int, default=25,							# Number of epochs the training should continue for
	help="Number of epochs the training should run for")
ap.add_argument("-p", "--plot", type=str, default="plot.png",					# Path for performance graph
	help="Path to output loss/accuracy plot")
args = vars(ap.parse_args())

########################### HYPERPARAMETERS ####################################

learning_rate = 1e-4
momentum = 0.9
decay = 1e-4
epochs = args["epochs"]
batch_size = 32
################################################################################

LABELS = set(["Choking", "notChoking"])										# Initializing labels from the set (The labels should match the folder names in dataset)
imagePaths = list(paths.list_images(args["dataset"]))							# Loading the images from our dataset

model = model.ActivityModel(batch_size)
model.loadData()
model.saveLabels(args["label-bin"])
trainX, testX, trainY, testY = model.splitAugmentData()
model.compile(lr, momentum, decay, epochs)
history = model.fit()

predictions = model.predict(x=testX.astype("float32"), batch_size=32)			# Applying predictions on test set
print(classification_report(testY.argmax(axis=1), predictions.argmax(axis=1), target_names=model.lb.classes_))

model.saveTrainingPlot(epochs, args["plot"])
model.save(args["model"], save_format="h5")
