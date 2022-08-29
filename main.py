import os
from dotenv import load_dotenv
import requests
import json
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

load_dotenv()

API_KEY = os.environ.get('API_KEY')


@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        return redirect(url_for('word_page', word=request.form.get('word')))
    return render_template("index.html")


@app.route("/<string:word>")
def word_page(word):
    headers = {
        "Authorization": f'Token {API_KEY}'
    }
    with requests.get(f'https://owlbot.info/api/v4/dictionary/{word}', headers=headers) as response:
        print("------------------------------------------------------------------")
        print(word)
        print("called")
        print(response.json())
        print("-------------------------------------------------------------------")
    return render_template('word.html', word=response.json())



if __name__ == "__main__":
    app.run(debug=True)
