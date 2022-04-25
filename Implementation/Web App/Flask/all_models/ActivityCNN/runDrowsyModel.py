############################# Necessary Utilities #############################

from tensorflow.keras.models import load_model
from collections import deque
import numpy as np
import argparse
import pickle
import cv2
import os

import firebase_utils

###############################################################################

cwd = os.path.abspath(os.getcwd())

model_path = cwd + "\\all_models\weights\drowsy\drowsy.model"
label_path = cwd + "\\all_models\weights\drowsy\drowsy_lb.pickle"

model = load_model(model_path)													# Loading the trained model from the disk
lb = pickle.loads(open(label_path, "rb").read())								# Loading the labels from the disk

def run(model_path, label_path, queue_size, images_folder, current_frame, current_seq, imagesList):

	mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")				# Intitializing the mean for mean subtraction
	Q = deque(maxlen=queue_size)													# Initializing the prediction queue

	(W, H) = (None, None)															# Image dimensions

	for frame in imagesList:
		if W is None or H is None:													# If frame dimensions are empty, grab them
			(H, W) = frame.shape[:2]

		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)								# Converting it into RGB
		frame = cv2.resize(frame, (224, 224)).astype("float32")						# Resizing it to a fixed dimension
		frame -= mean																# Performing mean subtraction

		preds = model.predict(np.expand_dims(frame, axis=0))[0]						# Make predictions on the frame
		#print(preds)
		Q.append(preds)																# Update the prediction queue

	results = np.array(Q).mean(axis=0)												# Performing predictions averaging over previous predictions
	i = np.argmax(results)
	label = lb.classes_[i]

	if label == 'Drowsy':
		firebase_utils.add_data("Drowsy Behaviour Detected")

	output = current_frame.copy()
	text = "Activity: {}".format(label)												# Write the predicted activity on the output frame
	cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_DUPLEX,					# Printing text on frame
		1, (255, 255, 255), 5)

	#cv2.imwrite("output.jpg", output)												# Saving frame (for testing purposes ONLY)

	print("Returning image")
	return output

def custom_start(model_path, label_path, queue_size, images_folder, current_frame, current_seq):

	imagesList = []

	for i in range(current_seq - queue_size, current_seq + 1):
		if i >= 0:
			img_name = images_folder + "\img" + str(i) + ".jpg"

			if os.path.exists(img_name):
				img = cv2.imread(img_name)
				imagesList.append(img)

	res = run(model_path, label_path, queue_size, images_folder, current_frame, current_seq, imagesList)
	return res
