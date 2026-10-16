import requests  # Import the requests library to handle HTTP requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
INPUT = lambda text_to_analyze: { "raw_document": { "text": text_to_analyze } }

def emotion_detector(text_to_analyze):
    response = requests.post(URL, json=INPUT(text_to_analyze), headers=HEADERS)
    return response.text