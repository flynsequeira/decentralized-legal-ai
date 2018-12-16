from flask import Flask, request
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions
import elasticsearch
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def hello():
        return "Hello World!"


@app.route("/api/search-case", methods=['GET'])
def search_case():
        search_string = request.args.get('search_string')
        es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
        # es.search(index='case_law', q='contract breach')
        result = es.search(index='case_law', q=search_string)
        searches = json.dumps(result)
        return searches



@app.route("/summarize-case", methods=['GET', 'POST'])
def summarize_case():
        if request.method == 'POST':
                natural_language_understanding = NaturalLanguageUnderstandingV1(version='2018-11-16',iam_apikey='fhfAp9h12U5DSbZ0AzPomZ-suKwnboNAg3EdorPHsB5e',url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api')
                response = natural_language_understanding.analyze(text=request.form.get('case_body'),features=Features(categories=CategoriesOptions(limit=3))).get_result()
                return response


if __name__ == "__main__":
        app.run()