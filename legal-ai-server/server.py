from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from elasticsearch import Elasticsearch
import bcrypt
import datetime
import requests
import json
import time

def connect():
    connection = MongoClient('localhost', 27017)
    handle = connection["flask_reminders"]
    return handle

app = Flask(__name__)
app.config['ELASTICSEARCH_URL'] = 'localhost:9200/'
es =  Elasticsearch([app.config['ELASTICSEARCH_URL']])
handle = connect()


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route('/case', methods=['POST'])
def data():
    key1 = request.get_json()
    print(key1['data'])

    return  "{status:error, data: 'test'}"


if __name__ == '__main__':
    app.run()