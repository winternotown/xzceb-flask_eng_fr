from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """
    This program translates english words to french.
    """
    textToTranslate = request.args.get('textToTranslate')
    french_translation = translator.english_to_french(textToTranslate)
    return french_translation

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """
    This program translates french words to english.
    """
    textToTranslate = request.args.get('textToTranslate')
    english_translation = translator.french_to_english(textToTranslate)
    return english_translation

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
