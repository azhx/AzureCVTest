import os
import requests
from flask import Flask, request, render_template, send_from_directory
import json
from PIL import Image
from io import BytesIO
from flask import Flask, render_template, request
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
subscription_key = "315a2e9c6d88414eb5a6d36eafc5c674"
'''MAKE SURE TO REMOVE THE KEY BEFORE PUSHING'''
assert subscription_key
vision_base_url = "https://eastus2.api.cognitive.microsoft.com/vision/v2.0/"
analyze_url = vision_base_url + "analyze"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    link = str(request.form['link'])
    text = azure(link)
    return render_template('index.html', url = link, text = text)

def azure(image_url):
    image_url  = image_url
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params = {'visualFeatures': 'Categories,Description,Color'}
    data = {'url': image_url}
    response = requests.post(analyze_url, headers=headers,
                             params=params, json=data)
    response.raise_for_status()
    analysis = response.json()
    return str(analysis)

if __name__ == '__main__':
   app.run()
