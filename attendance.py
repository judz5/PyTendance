import cv2
import numpy as np
import face_recognition
import os, csv, keyboard
from datetime import datetime

path = 'StudentImage'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for c1 in myList:
    curImg = cv2.imread(f'{path}/{c1}')
    images.append(curImg)
    classNames.append(os.path.splitext(c1)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        print(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
print('done')
cap = cv2.VideoCapture(0)

go = True

attendance = []

running = True

print("entering loop")
while running:

    success, img = cap.read(0)
    imgS = cv2.resize(img,(0,0),None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    if go:

        facesCurFrames = face_recognition.face_locations(imgS) # face locations
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrames) 

        for encodeFace, faceLoc, in zip(encodesCurFrame, facesCurFrames):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                if not name in attendance: attendance.append([name, datetime.now().strftime("%H:%M;%S")])
                print(name)
            else:
                name = "Unknown"

    go = not go

    for(top, right, bottom, left) in facesCurFrames:
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)

    try:
        if keyboard.is_pressed('q'):
            running = False
    except:
        pass


with open('attendanceSheet.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    wrtier.writerow(attendance)    