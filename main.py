import os
import requests
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")


@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        return redirect(url_for('word_page', word=request.form.get('word')))
    return render_template("index.html")


@app.route("/<word>")
def word_page(word):
    print("request method got---------------------------------------")
    headers = {
        "Authorization": f'Token {API_KEY}'
    }
    with requests.get(f'https://owlbot.info/api/v4/dictionary/{word}', headers=headers) as response:
        word_data = response.json()
    return render_template('word.html', word=word_data)
    # return word_data


if __name__ == "__main__":
    app.run(debug=True)
