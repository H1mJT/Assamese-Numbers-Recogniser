# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 20:38:00 2021

@author: Himjyoti
"""

import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

def recog_numbers(image):
    # Authenticate
    prediction_key = "64f49a8cf19f44f293287d6cc477c401"
    ENDPOINT = "https://assamesenumbers-prediction.cognitiveservices.azure.com/"

    
    base_image_location = os.path.join (os.path.dirname(__file__), "static")
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
    
    with open(os.path.join (base_image_location, 'tmp/' + image.filename), "rb") as image_contents:
        results = predictor.classify_image(
            'e7ea3663-53a3-4644-b52a-1b271839d6dc', 'Iteration1', image_contents.read())
       
    
       
        print('Actual Number= ৬\nPrediction of Image1:')
        i=0
        # Display the results.
        for prediction in results.predictions:
           
            i=i+1
            if i==1:
                r=prediction.tag_name
                
                
            else:
                break

    return r

#im=Image.open("test_image1.jpg")
#print(recog_numbers(im))
