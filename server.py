"""
This modules creates a flask app for an emotion detection webapp
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detector():
    """
    Pulls user's inputted text and returns a set of emotion scores and
    dominant emotion detected from the user's text using Watson's
    emotion model.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    dominant = emotions["dominant_emotion"]
    if dominant is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is 'anger': {anger}, 'disgust':"
            f" {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The "
            f"dominant emotion is {dominant}.")

@app.route("/")
def render_index_page():
    """
    Renders the home page of the emotion detection web app.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
