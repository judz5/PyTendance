import cv2
import numpy as np
import face_recognition
import os

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

print("entering loop")
while True:

    success, img = cap.read(0)
    imgS = cv2.resize(img,(0,0),None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    if go:

        facesCurFrames = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrames)

        for encodeFace, faceLoc, in zip(encodesCurFrame, facesCurFrames):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)

    go = not go

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)    