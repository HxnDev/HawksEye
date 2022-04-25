import cv2
import os
import pickle
import cvzone
import numpy as np
import keyboard

#for test1
#width, height = 36, 70

#for test2
width, height = 41, 75

#for test3
#width, height = 40, 80


def checkParkingSpace(imgPro, img, posList):

    spaceCounter = 0;

    for pos in posList:
        x, y = pos

        # cropping the images
        imgCrop = imgPro[y:y+height,x:x+width]
        # cv2.imshow(str(x*y), imgCrop)

        # count the pixels in each parking place
        count = cv2.countNonZero(imgCrop)

        # put count of pixels of each place in rectangles
        cvzone.putTextRect(img,str(count),(x-20,y+height-20), scale=0.5, thickness=1, offset=0, colorR=(0,0,255))


        if count < 200:
            color = (0,255,0)
            thickness = 5
            spaceCounter += 1
            cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, 2)

        else:
            color = (0,0,255)
            thickness = 2
            cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, 2)
        #print(count)



        #cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, 2)
        #cv2.rectangle(img, (x,y), (x+width,y+height), (0, 255, 0), 2)

    # put count of pixels of each place in rectangles
    #cv2.rectangle(img, pos, (pos[0]+width-10, pos[1]+height-10), color, thickness)
    cvzone.putTextRect(img, f'{spaceCounter}/{len(posList)}' ,(20, 30), scale=2, thickness=0, offset=5, colorR=color)

def custom_start(fullImagePath, fullLabelPath):

    with open(fullLabelPath, 'rb') as f:
        posList = pickle.load(f)

    img = cv2.imread(fullImagePath)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 1)

    # converting image to binary (white lines on black bg)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,25,16)

    # clear out the "noise" pixels
    imgMedian = cv2.medianBlur(imgThreshold, 5)

    kernel = np.ones((3,3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate, img, posList)

    return img
