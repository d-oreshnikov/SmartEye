from deepface import DeepFace
import cv2
import tempfile
import time
import psutil
import logging
import numpy as np
import pandas as pd
from collections import defaultdict
logging.basicConfig(filename='usage.log', level=logging.INFO)


def face_encoder(frame, model):
    return DeepFace.represent(img_path = frame, model_name=model, enforce_detection=False)[0]['embedding']


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



def verify(emb1 , emb2, model):
    return DeepFace.verify(emb1, emb2, model_name=model, silent=True)["verified"]




faceProto = "../models/opencv_face_detector.pbtxt"
faceModel = "../models/opencv_face_detector_uint8.pb"
faceNet = cv2.dnn.readNet(faceModel, faceProto)
tfile = tempfile.NamedTemporaryFile(delete=False)

data = {"name" : ["Margo", "Radcliffe", "Stone", "Stiller"], 
        "photo_path" : ["../photo/margo.jpeg", "../photo/Radcliffe.jpeg", "../photo/Stone.jpg", "../photo/Stiller.jpeg"], 
        "video_path" : ["../photo/margo.mp4", "../photo/Radcliffe.mp4", "../photo/Stone.mp4", "../photo/Stiller.mp4"]
        }
models = ["Facenet", "DeepFace", "ArcFace"]

result_data = {"Model": [], "Video": [], "Mean_CPU": [], "Used_Memory_GB": [], "Count": []}

for i in range(len(data["name"])):
    print(f"===============================Video: {data['name'][i]}============================")
    for model in models:
        print(f"===============================Model: {model}============================")
        video = cv2.VideoCapture(data["video_path"][i])
        last_execution_time = time.time()
        face_reference = face_encoder(data["photo_path"][i], model)

        while True:
            hasFrame, frame = video.read()
            if not hasFrame:  # Если конец видео
                print("Видео завершено. Переход к следующему видео.")
                break
            resultImg, faceBoxes = highlightFace(faceNet, frame)

            if faceBoxes and time.time() - last_execution_time >= 5:
                face_encodings = face_encoder(frame, model)

                if verify(face_encodings, face_reference, model):

                    memory = psutil.virtual_memory()
                    used_memory_gb = memory.used / (1024**3)
                    cpu_percentages = psutil.cpu_percent(percpu=True)

                    result_data["Model"].append(model)
                    result_data["Video"].append(data["name"][i])
                    result_data["Mean_CPU"].append(np.mean(cpu_percentages))
                    result_data["Used_Memory_GB"].append(used_memory_gb)
                    result_data["Count"].append(True)
                    print(f'{model},{data["name"][i]},{np.mean(cpu_percentages)},{used_memory_gb},{True}')
                else:
                    pass
                last_execution_time = time.time()


# Создаем DataFrame
df = pd.DataFrame(result_data)

# Выводим DataFrame на экран
df.to_csv("output.csv")