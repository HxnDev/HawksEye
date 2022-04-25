###################### IMPORTS #######################

import os
import cv2
import sys
import time
import threading

from flask_cors import CORS
from flask import Flask, Response
from flask_restful import Api, Resource, reqparse

import myutils
import run_models

###################### FLASK INITIALISATION #######################

app = Flask(__name__)
CORS(app)
api = Api(app)

###################### START #######################

# initialize a lock used to ensure thread-safe
# exchanges of the frames (useful for multiple browsers/tabs
# are viewing tthe stream)
lock = threading.Lock()

# global var to keep track of current model selected
model_selection = [None]

###################### SELECTION ROUTE #######################
@app.route('/selectModel', methods = ['GET', 'POST'])
def selectModel():
    # get and parse the arguments sent in the request from frontend
    parser = reqparse.RequestParser()
    parser.add_argument('type', type=str)
    args = parser.parse_args()
    print("Args: ", args)

    # update model selection
    request_type = args['type']
    model_selection[0] = request_type
    print("Model selection: ", model_selection[0])

    # return json message to frontend
    response = {"status": "Success", "message": "Selected model changed"}

    # wipe out all previously stored frames
    cwd = os.path.abspath(os.getcwd())
    myutils.clear_directory(cwd + "\models\images")

    return response


###################### RETURN IMG ROUTE #######################
@app.route('/init', methods = ['GET'])
def init():
    cwd = os.path.abspath(os.getcwd())
    myutils.clear_directory(cwd + "\\all_models\images")

    # return json message to frontend
    response = {"status": "Success", "message": "Flask initialised"}
    return response

@app.route('/stream',methods = ['GET'])
def stream():
   return Response(generateStream(), mimetype = "multipart/x-mixed-replace; boundary=frame")

def generateStream():
    # we use this function attribute to keep track of sequence number of current images
    # this is just for storing images, not required if you only need current image
    if not hasattr(generateStream, 'img_name_seq'):
        generateStream.img_name_seq = -1

    # grab global references to the lock variable
    global lock

    # initialize the video stream
    vc = cv2.VideoCapture(0)

    # check camera is open
    if vc.isOpened():
        rval, frame = vc.read()

    else:
        rval= False

    # while streaming
    while rval:
        frame_rate = 30
        prev = 0

        # wait until the lock is acquired
        with lock:
            # read next frame
            rval, frame = vc.read()
            time_elapsed = time.time() - prev

            # if a model has been selectied
            if model_selection[0] is not None:

                # increment sequence
                generateStream.img_name_seq += 1

                # get absolute path of current directory
                cwd = os.path.abspath(os.getcwd())
                # we need the path of where to save the image
                fullImagePath = cwd + '\\all_models\images\img' + str(generateStream.img_name_seq) + '.jpg'

                # save image
                cv2.imwrite(fullImagePath, frame)

                if time_elapsed > 1. / frame_rate:
                    prev = time.time()

                    # if blank frame
                    if frame is None:
                        continue

                    # call script for running model and recieving the predicted img
                    if (model_selection[0] == 'yolo-empty'):
                        predicted_img = run_models.run_empty_counter(fullImagePath)

                        (flag, img) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(img) + b'\r\n')

                    elif (model_selection[0] == 'yolo-weapon'):
                        predicted_img = run_models.run_weapon(fullImagePath)

                        (flag, img) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(img) + b'\r\n')

                    elif (model_selection[0] == 'face-mask'):
                        predicted_img = run_models.run_face_mask(fullImagePath, generateStream.img_name_seq, frame)

                        (flag, img) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(img) + b'\r\n')

                    elif (model_selection[0] == 'yolo-social-dist'):
                        predicted_img = run_models.run_social_dist(fullImagePath, generateStream.img_name_seq)

                        (flag, img) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(img) + b'\r\n')

                    elif (model_selection[0] == 'activity-faint'):
                        images_folder = cwd + "\\all_models\images"
                        predicted_img = run_models.run_faint_model(images_folder, frame, generateStream.img_name_seq)

                        (flag, encodedImage) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

                    elif (model_selection[0] == 'activity-choke'):
                        images_folder = cwd + "\\all_models\images"
                        predicted_img = run_models.run_choke_model(images_folder, frame, generateStream.img_name_seq)

                        (flag, encodedImage) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

                    elif (model_selection[0] == 'activity-drowsy'):
                        images_folder = cwd + "\\all_models\images"
                        predicted_img = run_models.run_drowsy_model(images_folder, frame, generateStream.img_name_seq)

                        (flag, encodedImage) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

                    elif (model_selection[0] == 'activity-aggressive'):
                        images_folder = cwd + "\\all_models\images"
                        predicted_img = run_models.run_aggressive_model(images_folder, frame, generateStream.img_name_seq)

                        (flag, encodedImage) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

                    elif (model_selection[0] == 'activity-smoking'):
                        images_folder = cwd + "\\all_models\images"
                        predicted_img = run_models.run_smoking_model(images_folder, frame, generateStream.img_name_seq)

                        (flag, encodedImage) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

                    elif (model_selection[0] == 'yolo-person'):
                        predicted_img = run_models.run_isolation_ward(fullImagePath)

                        (flag, img) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(img) + b'\r\n')

                    elif (model_selection[0] == 'car-parking'):
                        predicted_img = run_models.run_car_parking(fullImagePath)

                        (flag, img) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(img) + b'\r\n')

                    elif (model_selection[0] == 'face-attendance'):
                        predicted_img = run_models.run_face_attendance(fullImagePath)

                        (flag, img) = cv2.imencode(".jpg", predicted_img)
                        # yield the output frame in the byte format
                        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(img) + b'\r\n')


            else:
                (flag, encodedImage) = cv2.imencode(".jpg", frame)
                # yield the output frame in the byte format
                yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

    # release the camera
    vc.release()
