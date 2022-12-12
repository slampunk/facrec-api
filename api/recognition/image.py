# import the necessary packages
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2
import base64
import os
import numpy as np
from functools import reduce

# Create your models here.
def RunRecognition(recognitionRequest):
    result = { "traderId": recognitionRequest["traderId"], "confidence": 0 }
    data = pickle.loads(open("recognition/encodings/model.enc", "rb").read())
    candidateEncodings = get_candidate_encodings(recognitionRequest["traderId"], data)
    if not candidateEncodings:
        return result

    [ encodings, boxes ] = get_computed_encodings(recognitionRequest["image"])

    for (index, encoding) in enumerate(encodings):
        matches = face_recognition.compare_faces(candidateEncodings,
			encoding)
        distance = face_recognition.face_distance(candidateEncodings,
             encoding)

        print(recognitionRequest["traderId"])
        print(distance)

        if True in matches:
            distance = face_recognition.face_distance(candidateEncodings,
                encoding)
            result["confidence"] = max(result["confidence"], 1 - round(min(distance), 4))
            (top, right, bottom, left) = boxes[index]
            result["location"] = {"top": top.item(), "bottom": bottom.item(), "right": right.item(), "left": left.item()}

    return result

def get_candidate_encodings(target, data):
    encodingIndices = list(map(lambda name : 1 if name == target else 0, data["names"]))
    return [entry for index, entry in enumerate(data["encodings"]) if encodingIndices[index] == 1]

def get_computed_encodings(imageData):
    nparr = np.fromstring(base64.b64decode(imageData), np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    detector = cv2.CascadeClassifier("recognition/cascades/haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30))
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
    return [ face_recognition.face_encodings(rgb, boxes), boxes ]
