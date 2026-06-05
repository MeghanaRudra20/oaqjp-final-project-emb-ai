import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=myobj, headers=headers)

    response_dict = response.json()

    anger = response_dict['emotionPredictions'][0]['emotion']['anger']
    disgust = response_dict['emotionPredictions'][0]['emotion']['disgust']
    fear = response_dict['emotionPredictions'][0]['emotion']['fear']
    joy = response_dict['emotionPredictions'][0]['emotion']['joy']
    sadness = response_dict['emotionPredictions'][0]['emotion']['sadness']

    dominant_emotion = max(
        {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        },
        key=lambda x: {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }[x]
    )

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
    