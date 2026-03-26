"""This module is for holding the emotion_detector function"""
import requests
import json

def emotion_detector(text_to_analyze:str) -> dict:
    """This function is for interpreting the emotion of the str input"""

    # Constructing the request payload
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    request_body = {"raw_document": { "text": text_to_analyze }}
    request_headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detector API
    response = requests.post(url, json=request_body, headers=request_headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 200: 
        # In case of status_code 200 display emotions dict 
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        emotions['dominant_emotion'] = max(emotions,key=emotions.get)
    elif response.status_code == 400:
        # In case of empty input return a response with null values
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return emotions
