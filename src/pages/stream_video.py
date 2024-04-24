import streamlit as st
import numpy as np
import cv2
import tempfile
from utils.encoder import face_encoder, verify
from database.pgadd import get_card_info, get_photo
import time

models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib", "ArcFace"]

def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
    net.setInput(blob)
    detections = net.forward()
    faceBoxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            faceBoxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn, faceBoxes

faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"
faceNet = cv2.dnn.readNet(faceModel, faceProto)
st.title("Camera input")
tfile = tempfile.NamedTemporaryFile(delete=False)
video = cv2.VideoCapture("photo/margo.mp4")
frameST = st.empty()
last_execution_time = time.time()

col1, col2 = st.columns([3, 1])  # Определение колонок: 3 для камеры, 1 для изображения

while True:
    hasFrame, frame = video.read()
    resultImg, faceBoxes = highlightFace(faceNet, frame)

    if faceBoxes and time.time() - last_execution_time >= 5:
        face_encodings = face_encoder(frame)

        closest_hash, closest_status = verify(face_encodings)
        res = get_card_info("cards_meta", closest_hash)

        name = str(closest_status['verified'])
        if name == "True":
            with col1:

                nparr = np.frombuffer(get_photo(closest_hash), np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                st.image(img, channels='BGR', width=200)
                st.text(f"Лицо найдено! ФИО: {res[0][0]} {res[0][1]} {res[0][2]}") 
        else:
            with col1:
                st.text(f"Лицо не найдено! Самое близкое к нему {res} с точностью {closest_status}")
        last_execution_time = time.time()
    frameST.image(resultImg, channels="BGR")

