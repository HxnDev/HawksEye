############################# Necessary Utilities #############################

from tensorflow.keras.models import load_model
from collections import deque
import numpy as np
import argparse
import pickle
import cv2
###############################################################################

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()													# Designing some arguments
ap.add_argument("-m", "--model", required=True,									# Path to trained model
	help="Path to trained model")
ap.add_argument("-l", "--label-bin", required=True,								# Path to labels
	help="Path to  labels")
ap.add_argument("-i", "--input", required=True,									# Path to input video
	help="Path to our input video")
ap.add_argument("-o", "--output", required=True,								# Path to output video
	help="Path to our output video")
ap.add_argument("-s", "--size", type=int, default=128,							# Size of queue
	help="Size of queue for averaging")
args = vars(ap.parse_args())

print("Loading model and labels...")
model = load_model(args["model"])												# Loading the trained model from the disk
lb = pickle.loads(open(args["label_bin"], "rb").read())							# Loading the labels from the disk
mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")				# Intitializing the mean for mean subtraction
Q = deque(maxlen=args["size"])													# Initializing the prediction queue

vs = cv2.VideoCapture(args["input"])											# Initializing the video stream (Type 0  for webcam)
writer = None
(W, H) = (None, None)															# Video dimensions

while True:																		# Looping over every frame in the video
	(grabbed, frame) = vs.read()												# Read the frame
	if not grabbed:																# If no frame is read, the video is ended
		break
	if W is None or H is None:													# If frame dimensions are empty, grab them
		(H, W) = frame.shape[:2]

	output = frame.copy()														# Cloning the output frame
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)								# Converting it into RGB
	frame = cv2.resize(frame, (224, 224)).astype("float32")						# Resizing it to a fixed dimension
	frame -= mean																# Performing mean subtraction

	preds = model.predict(np.expand_dims(frame, axis=0))[0]						# Make predictions on the frame
	Q.append(preds)																# Update the prediction queue
	results = np.array(Q).mean(axis=0)											# Performing predictions averaging over previous predictions
	i = np.argmax(results)
	label = lb.classes_[i]

	text = "Activity: {}".format(label)											# Write the predicted activity on the output frame
	cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_DUPLEX,				# Printing text on frame
		1, (0, 0, 0), 5)

	if writer is None:															# Checking if video writer is currently none
		fourcc = cv2.VideoWriter_fourcc(*"MJPG")								# Initializing our video writer
		writer = cv2.VideoWriter(args["output"], fourcc, 30,					# Writing the output video
			(W, H), True)
	writer.write(output)														# Exporting the video to the disk
	cv2.imshow("Output", output)												# Display the video while exporting
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):															# If "q" is pressed, stop the loop
		break

print("Cleaning up...")															# Releasing the file pointers
writer.release()
vs.release()
