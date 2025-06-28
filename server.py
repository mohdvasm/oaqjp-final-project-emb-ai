"""
This module contains the emotion_detector function which sends text input to
the Watson NLP EmotionPredict API and returns emotion scores including the dominant emotion.
"""


from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """
    Homepage
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """
    Function to analyze the emotion with emotion
    detector
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    detected_emotions = emotion_detector(text_to_analyze)
    print(f"Detected emotions: {detected_emotions}")
    dominant_emotion = detected_emotions.pop("dominant_emotion")

    emotion_parts = [f"{emotion}: {score}" for emotion, score in detected_emotions.items()]
    formatted_emotions = ", ".join(emotion_parts)

    response = (
        f"For the given statement response is {formatted_emotions}. "
        f"The dominant emotion is {dominant_emotion}"
    )
    return response, 200


if __name__ == "__main__":
    app.run(port=5001, debug=True)
