from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
import string
import requests
import os

app = Flask(__name__)

load_dotenv()

API_KEY = os.environ.get('API_KEY')

@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        return redirect(url_for('word_page', word=request.form.get('word')))
    return render_template("index.html")


@app.route("/word/<string:word>")
def word_page(word):
    headers = {
        "Authorization": f'Token {API_KEY}'
    }
    with requests.get(f'https://owlbot.info/api/v4/dictionary/{word}', headers=headers) as response:
        if response.status_code != 200 or word[0].lower() not in list(string.ascii_lowercase):
            return render_template('not_found.html', error=response.status_code)
    return render_template('word.html', word=response.json())



if __name__ == "__main__":
    app.run(debug=True)
