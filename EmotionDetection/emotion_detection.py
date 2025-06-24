import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)

    formatted_response = json.loads(response.text)
    dictionary = {}
    #print("status code")
    #print(response.status_code)

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        #output = "{\n"        

        for key, value in emotions.items():
            #output += f"'{key}': {value},\n"
            dictionary.update({key: value})

        #anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        dominant_emotion = max(emotions, key=emotions.get)
        dictionary["dominant_emotion"] = dominant_emotion
        #output += "'dominant_emotion': '" + dominant_emotion + "'"
        #output += "\n}"

    elif response.status_code == 400:
        #print("It is none")
        #dictionary = None
        #print(dictionary)
        ##return None
        dictionary = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    #print(output)
    return dictionary