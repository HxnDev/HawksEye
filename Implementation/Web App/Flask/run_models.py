###################### IMPORTS #######################

import os
import cv2
import sys
import shlex
import subprocess

# Adding paths of model files so we can import them
cwd = os.path.abspath(os.getcwd())
sys.path.append(cwd + '\all_models\ActivityCNN')

# import model files
from all_models.ActivityCNN import runDrowsyModel, runFaintModel, runChokeModel, runSmokingModel, runAggressiveModel
from yolov5_person import detect
from yolov5_weapon import detect_weapon
from faceMask import detect_mask
from carParking import detect_parking
from faceAttendance import face_recognizer

#####################################################

def run_empty_counter(fullImagePath):
    # we need to know the paths of data and model
    fullModelPath = cwd + "\\all_models\weights\empty_counter_weights.pt"
    fullDataPath = cwd + "\\all_models\data\person.yaml"

    # pass image path and model path to yolo
    predicted_img = detect.custom_start(fullModelPath, fullImagePath, fullDataPath)

    # delete image (no longer needed)
    # os.remove(fullImagePath)

    # return image with predictions overlay
    return predicted_img

def run_face_mask(fullImagePath, img_seq, image):

    cwd = os.path.abspath(os.getcwd())
    sys.path.append(cwd + '\\faceMask')

    fullDetectPath = cwd + "\\faceMask\detect_mask.py"
    fullModelPath = cwd + '\\all_models\\weights\\face_mask_weights.pth'
    fullSavedPath = cwd + "\\faceMask\inference" + "\img" + str(img_seq) + ".jpg"

    p = subprocess.Popen(['python', fullDetectPath, '--img-path', fullImagePath, '--output-path', fullSavedPath, '--weights', fullModelPath])
    p.communicate()

    predicted_img = cv2.imread(fullSavedPath)

    return predicted_img

def run_social_dist(fullImagePath, img_seq):
    # get absolute path of current directory
    cwd = os.path.abspath(os.getcwd())

    fullModelPath = cwd + "\\all_models\weights\social_distancing_weights.pt"
    fullDetectPath = cwd + "\\all_models\yolo-social-distancing\detect.py"

    outputPath = cwd + "\\all_models\yolo-social-distancing\inference\output"
    P = subprocess.Popen(['python', fullDetectPath, '--source', fullImagePath, '--weights', fullModelPath, '--output', outputPath])
    P.communicate()

    fullSavedPath = cwd + "\\all_models\yolo-social-distancing\inference\output" + "\img" + str(img_seq) + ".jpg"
    predicted_img = cv2.imread(fullSavedPath)

    return predicted_img

def run_faint_model(images_folder, current_frame, current_seq, queue_size=15):
    # get absolute path of current directory
    cwd = os.path.abspath(os.getcwd())

    # provide paths of model and label files
    model_path = cwd + "\\all_models\weights\\faint\\faint.model"
    label_path = cwd + "\\all_models\weights\\faint\\faint_lb.pickle"

    # print('model path: ', model_path)
    # print('label path: ', label_path)

    predicted_img = runFaintModel.custom_start(model_path, label_path, queue_size, images_folder, current_frame, current_seq)

    # return image with predictions overlay
    return predicted_img

def run_choke_model(images_folder, current_frame, current_seq, queue_size=15):
    # get absolute path of current directory
    cwd = os.path.abspath(os.getcwd())

    # provide paths of model and label files
    model_path = cwd + "\\all_models\weights\choke\choke.model"
    label_path = cwd + "\\all_models\weights\choke\choke_lb.pickle"

    # print('model path: ', model_path)
    # print('label path: ', label_path)

    predicted_img = runChokeModel.custom_start(model_path, label_path, queue_size, images_folder, current_frame, current_seq)

    # return image with predictions overlay
    return predicted_img

def run_drowsy_model(images_folder, current_frame, current_seq, queue_size=15):
    # get absolute path of current directory
    cwd = os.path.abspath(os.getcwd())

    # provide paths of model and label files
    model_path = cwd + "\\all_models\weights\drowsy\drowsy.model"
    label_path = cwd + "\\all_models\weights\drowsy\drowsy_lb.pickle"

    # print('model path: ', model_path)
    # print('label path: ', label_path)

    predicted_img = runDrowsyModel.custom_start(model_path, label_path, queue_size, images_folder, current_frame, current_seq)

    # return image with predictions overlay
    return predicted_img

def run_smoking_model(images_folder, current_frame, current_seq, queue_size=15):
    # get absolute path of current directory
    cwd = os.path.abspath(os.getcwd())

    # provide paths of model and label files
    model_path = cwd + "\\all_models\weights\smoking\smoking.model"
    label_path = cwd + "\\all_models\weights\smoking\smoking_lb.pickle"

    # print('model path: ', model_path)
    # print('label path: ', label_path)

    predicted_img = runSmokingModel.custom_start(model_path, label_path, queue_size, images_folder, current_frame, current_seq)

    # return image with predictions overlay
    return predicted_img

def run_aggressive_model(images_folder, current_frame, current_seq, queue_size=15):
    # get absolute path of current directory
    cwd = os.path.abspath(os.getcwd())

    # provide paths of model and label files
    model_path = cwd + "\\all_models\weights\\aggressive\\aggressive.model"
    label_path = cwd + "\\all_models\weights\\aggressive\\aggressive_lb.pickle"

    # print('model path: ', model_path)
    # print('label path: ', label_path)

    predicted_img = runAggressiveModel.custom_start(model_path, label_path, queue_size, images_folder, current_frame, current_seq)

    # return image with predictions overlay
    return predicted_img

def run_isolation_ward(fullImagePath):
    # we need to know the paths of data and model
    cwd = os.path.abspath(os.getcwd())
    fullModelPath = cwd + "\\all_models\weights\empty_counter_weights.pt"
    fullDataPath = cwd + "\\all_models\data\person.yaml"

    # pass image path and model path to yolo
    predicted_img = detect.custom_start(fullModelPath, fullImagePath, fullDataPath, alertOnPerson=True)

    # delete image (no longer needed)
    # os.remove(fullImagePath)

    # return image with predictions overlay
    return predicted_img

def run_car_parking(fullImagePath):

    cwd = os.path.abspath(os.getcwd())
    fullLabelPath = cwd + "\\carParking\\CarParkPosTest2"

    predicted_img = detect_parking.custom_start(fullImagePath, fullLabelPath)

    return predicted_img

def run_face_attendance(fullImagePath):

    cwd = os.path.abspath(os.getcwd())
    trainerPath = cwd + "\\faceAttendance\\trainer.yml"
    haarPath = cwd + "\\faceAttendance\\haarcascade_frontalface_default.xml"
    attendancePath = cwd + "\\faceAttendance\\Attendance.csv"

    predicted_img = face_recognizer.custom_start(fullImagePath, trainerPath, haarPath, attendancePath)

    return predicted_img

def run_weapon(fullImagePath):
    cwd = os.path.abspath(os.getcwd())
    # we need to know the paths of data and model
    fullModelPath = cwd + "\\all_models\weights\weapon.pt"
    fullDataPath = cwd + "\\all_models\data\weapon.yaml"

    # pass image path and model path to yolo
    predicted_img = detect_weapon.custom_start(fullModelPath, fullImagePath, fullDataPath)

    # delete image (no longer needed)
    # os.remove(fullImagePath)

    # return image with predictions overlay
    return predicted_img
