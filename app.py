
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:55:42 2021

@author: Himjyoti
"""

from recog_numbers import recog_numbers
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
        image.save(image_path)        

        response = recog_numbers(image)


        return render_template('recognize.html', predictions=response, image=url_for('static', filename='tmp/' + image.filename))
    else:
        return render_template('index.html')
