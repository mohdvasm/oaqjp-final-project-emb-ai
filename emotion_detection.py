import requests
import json 

# The URL endpoint
url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

# Headers with the model ID
headers = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(
    text_to_analyze: str
):
    try:
        # Input JSON payload
        payload = {
            "raw_document": {
                "text": text_to_analyze
            }
        }

        # Make the POST request
        response = requests.post(url, headers=headers, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            print("Success!")
            # print(response.json())
        else:
            print("Error:", response.status_code)
            # print(response.text)  

        # Parse JSON if input is a string
        if isinstance(response.text, str):
            emotion_data = json.loads(response.text)
        
        # Extract the emotion scores from the first prediction
        emotions = emotion_data["emotionPredictions"][0]["emotion"]
        
        # Find the emotion with the highest score
        dominant_emotion = max(emotions.items(), key=lambda x: x[1])

        emotions.update({
            "dominant_emotion": dominant_emotion[0]
        })
        # print(emotions)
        
        return emotions  

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # The text you want to analyze
    text_to_analyze = "I love this new technology."

    # Calling function 
    analysis = emotion_detector(
        text_to_analyze=text_to_analyze
    )

    print(analysis)