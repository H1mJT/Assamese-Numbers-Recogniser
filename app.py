
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:55:42 2021

@author: Himjyoti
"""


from recog_numbers import recog_numbers
from to_english import to_english
import os
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recognize', methods=['GET', 'POST'])
def recognize():
    if request.method == 'POST':
        # Get image
        image = request.files['image']
        # Create tmp directory if not existent
        if not os.path.exists(os.path.join('static', 'tmp')):
            os.mkdir(os.path.join('static', 'tmp'))

        # Save image
        image_path = os.path.join('static', 'tmp', image.filename)
        image.seek(0)
        try:
            image.save(image_path)
        except:
            return render_template('index.html', res="Please Select an Image")
        try:
            response,b = recog_numbers(image)
            eng=to_english(response)
        except:
            return render_template('index.html', res="Please Select a supported file type.")
        c=55
  
        return render_template('recognize.html',c=c, predictions=response,prob=b, eng=eng , image=url_for('static', filename='tmp/' + image.filename))
    else:
        return render_template('index.html')
