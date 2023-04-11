import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apiKey = os.environ['apiKey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey=apiKey)
language_translator = LanguageTranslatorV3(
  version='2018-05-01',
  authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
  """
  This function translates english to french
  """

  tranlate_json = language_translator.translate(
    text=englishText,
    model_id='en-fr'
  ).get_result()

  res = json.dumps(tranlate_json, indent=2, ensure_ascii=False)
  res = json.loads(res)
  frenchText = res["translations"][0]["translation"]

  return frenchText

def frenchToEnglish(frenchText):
  """
  This function translates french to english
  """

  tranlate_json = language_translator.translate(
    text=frenchText,
    model_id='fr-en'
  ).get_result()

  res = json.dumps(tranlate_json, indent=2, ensure_ascii=False)
  res = json.loads(res)
  englishText = res["translations"][0]["translation"]

  return englishText
