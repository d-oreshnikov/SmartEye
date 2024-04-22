from deepface import DeepFace
from database.pgadd import get_dict_from_database, get_card_info

models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib", "ArcFace"]


def face_encoder(frame):
    return DeepFace.represent(img_path = frame, model_name=models[6], enforce_detection=False)[0]['embedding']


def verify(emb1):
    cards = get_dict_from_database("cards_meta","photo_id", "embedding")

    min_distance = float('inf')

    for hash, emb2 in cards.items():
        status = DeepFace.verify(emb1, emb2, model_name=models[6])


        if status["distance"] < min_distance:
            min_distance = status["distance"]
            closest_status = status
            closest_hash = hash
    return closest_hash, closest_status

