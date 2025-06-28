from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():

    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Please provide a 'text' query parameter.", 400

    detected_emotions = emotion_detector(text_to_analyze)
    dominant_emotion = detected_emotions.pop("dominant_emotion")

    emotion_parts = [f"{emotion}: {score}" for emotion, score in detected_emotion.items()]
    formatted_emotions = ", ".join(emotion_parts)

    response = f"For the given statement response is {formatted_emotions}. The dominant emotion is {dominant_emotion['dominant_emotion']}"
    return response


if __name__ == "__main__":
    app.run(port=5000)
