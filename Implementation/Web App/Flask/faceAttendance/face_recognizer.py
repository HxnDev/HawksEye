import cv2
import numpy as np
import os
from datetime import datetime

def markAttendance(attendancePath, name):
    with open(attendancePath,'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'{name}, {time}, {date}\n')

def custom_start(fullImagePath, trainerPath, haarPath, attendancePath):

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(trainerPath)

    faceCascade = cv2.CascadeClassifier(haarPath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 0
    # names related to ids: The names associated to the ids: 1 for Mohamed, 2 for Jack, etc...
    names = ['Azka Khurram','Sana Khan','Tayyab Abbas','Abeera Fatima','Hassan Shahzad','Talha Mustafa','Nameira Rana'] # add a name into this list

    img = cv2.imread(fullImagePath)
    height, width, channels = img.shape

    minW = 0.1 * height
    minH = 0.1 * width

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        
        if (confidence <= 100):
            id = names[id]
            confidence = "  {0}%".format(round(100-confidence))
            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
            
        
        else:
            # Unknown Face
            id = "Unknown"
            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        #    confidence = "  {0}%".format(round(confidence))
        
        if id != 'Unknown':
            markAttendance(attendancePath, id)

    return img
