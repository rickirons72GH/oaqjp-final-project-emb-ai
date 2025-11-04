import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion detector API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract information
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
  
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']

        dom_emotion = max(emotions, key=emotions.get)
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dom_emotion = None

    emotion_scores = { 'anger': anger_score, 'disgust': disgust_score,'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dom_emotion }

    return emotion_scores