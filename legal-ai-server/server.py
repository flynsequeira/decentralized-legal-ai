from flask import Flask, request
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/summarize-case", methods=['GET', 'POST'])
def summarize_case():
    if request.method == 'POST':
        natural_language_understanding = NaturalLanguageUnderstandingV1(version='2018-11-16',iam_apikey='fhfAp9h12U5DSbZ0AzPomZ-suKwnboNAg3EdorPHsB5e',url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api')
        response = natural_language_understanding.analyze(text=request.form.get('case_body'),features=Features(categories=CategoriesOptions(limit=3))).get_result()
        return response


if __name__ == "__main__":
    app.run()