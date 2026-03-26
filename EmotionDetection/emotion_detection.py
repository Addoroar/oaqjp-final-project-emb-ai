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
    
    # Formatting the response into json
    formatted_response = json.loads(response.text)

    #Returning the first item from the emotionPredictions list
    return formatted_response['emotionPredictions'][0]['emotion']
