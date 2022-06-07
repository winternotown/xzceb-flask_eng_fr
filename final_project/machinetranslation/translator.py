""" This module translates words from English to French.
And French to English """
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This program translates english words to french.
    """
    french_text = language_translator.translate(
        text = english_text,
        model_id='en-fr').get_result()
    french_translation = french_text['translations'][0]['translation']
    return french_translation

def french_to_english(french_text):
    """
    This program translates french words to english.
    """
    english_text = language_translator.translate(
        text = french_text,
        model_id='fr-en').get_result()
    english_translation = english_text['translations'][0]['translation']
    return english_translation
