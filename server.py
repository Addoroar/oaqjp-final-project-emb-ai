"""This is the flask server file"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/")
def index_template():
    """This function renders the index template"""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    """This function takes a string as input analyzes it and returns a dict of emotions from it"""
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)

    # Error-handling in case of no input
    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (f"For the statement, the system response is 'anger': {emotions['anger']}, "
            f"'disgust':{emotions['disgust']}, 'fear':{emotions['fear']}, "
            f"'joy':{emotions['joy']}, 'sadness':{emotions['sadness']}. "
            f"The dominant emotion is {emotions['dominant_emotion']}")

if __name__ == "main":
    app.run(host="0.0.0.0",port=5000)
