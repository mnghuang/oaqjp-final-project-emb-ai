import requests
import json

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
INPUT = lambda text_to_analyze: { "raw_document": { "text": text_to_analyze } }

def emotion_detector(text_to_analyze):
    response = requests.post(URL, json=INPUT(text_to_analyze), headers=HEADERS)
    if response.status_code == 400:
        emotions = {"anger":None, "disgust":None, "fear":None, "joy":None, "sadness":None, "dominant_emotion":None}
    else:
        formatted = json.loads(response.text)
        anger = float(formatted["emotionPredictions"][0]["emotion"]["anger"])
        disgust = float(formatted["emotionPredictions"][0]["emotion"]["disgust"])
        fear = float(formatted["emotionPredictions"][0]["emotion"]["fear"])
        joy = float(formatted["emotionPredictions"][0]["emotion"]["joy"])
        sadness = float(formatted["emotionPredictions"][0]["emotion"]["sadness"])
        emotions = {"anger":anger, "disgust":disgust, "fear":fear, "joy":joy, "sadness":sadness}
        emotions["dominant_emotion"] = max(emotions, key=emotions.get)
    return emotions
