from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french(english_text):
    """
    This program translates english words to french.
    """
    french_text = language_translator.translate(
        text = english_text,
        model_id='en-fr').get_result()
    french_translation = french_text['translations'][0]['translation']
    return french_translation

@app.route("/french_to_english")
def french_to_english(french_text):
    """
    This program translates french words to english.
    """
    english_text = language_translator.translate(
        text = french_text,
        model_id='fr-en').get_result()
    english_translation = english_text['translations'][0]['translation']
    return english_translation

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)