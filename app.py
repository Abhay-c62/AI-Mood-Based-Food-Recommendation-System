from flask import Flask, render_template, request

from model.sentiment import detect_mood
from model.recommender import recommend_food

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    user_text = request.form["mood"]

    mood = detect_mood(user_text)

    foods = recommend_food(mood)

    return render_template(
        "result.html",
        mood=mood,
        user_text=user_text,
        foods=foods
    )


if __name__ == "__main__":

    app.run(debug=True)