# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:55:42 2021

@author: Himjyoti
"""
from flask import Flask
app = Flask(__name__)

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os
import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img

@app.route("/")
def func():
    
    ENDPOINT = "https://assamesenumbers-prediction.cognitiveservices.azure.com/"
    prediction_key = "64f49a8cf19f44f293287d6cc477c401"
    prediction_resource_id = "/subscriptions/adca6350-a85d-43d1-a0ed-be51a4efc45a/resourceGroups/Assamese-Numbers/providers/Microsoft.CognitiveServices/accounts/AssameseNumbers"
    
    base_image_location = os.path.join (os.path.dirname(__file__), "Images")
    
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
    
    # Now there is a trained endpoint that can be used to make a prediction
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
    
    with open(os.path.join (base_image_location, "Test/test_image1.jpg"), "rb") as image_contents:
        results = predictor.classify_image(
            'e7ea3663-53a3-4644-b52a-1b271839d6dc', 'Iteration1', image_contents.read())
       
    
       
        plt.figure()
        plt.clf()
        plt.imshow(load_img("Images/Test/test_image1.jpg"), cmap = 'Greys')
        plt.xlabel('Image1')
        print('Actual Number= ৬\nPrediction of Image1:')
        i=0
        # Display the results.
        for prediction in results.predictions:
           
            i=i+1
            if i==1:
                r=prediction.tag_name
                s=prediction.probability * 100
                print("\t" + prediction.tag_name +
                      ": {0:.2f}%".format(prediction.probability * 100))
            else:
                break
    
    with open(os.path.join (base_image_location, "Test/test_image2.jpg"), "rb") as image_contents:
        results = predictor.classify_image(
            'e7ea3663-53a3-4644-b52a-1b271839d6dc', 'Iteration1', image_contents.read())
       
    
       
        plt.figure()
        plt.clf()
        plt.imshow(load_img("Images/Test/test_image2.jpg"), cmap = 'Greys')
        plt.xlabel('Image2')
        print('Actual Number= ২\nPrediction of image2:')
        # Display the results.
        i=0
        for prediction in results.predictions:
            i=i+1
            if i==1:
                q=prediction.tag_name
                w=prediction.probability * 100
                print("\t" + prediction.tag_name +
                      ": {0:.2f}%".format(prediction.probability * 100))
            else:
                break
    
    with open(os.path.join (base_image_location, "Test/test_image3.jpg"), "rb") as image_contents:
        results = predictor.classify_image(
            'e7ea3663-53a3-4644-b52a-1b271839d6dc', 'Iteration1', image_contents.read())
       
    
       
        plt.figure()
        plt.clf()
        plt.imshow(load_img("Images/Test/test_image3.jpg"), cmap = 'Greys')
        plt.xlabel('Image3')
        print('Actual Number= ৯\nPrediction of Image 3:')
        # Display the results.
        i=0
        for prediction in results.predictions:
            i=i+1
            if i==1:
                a=prediction.tag_name
                b=prediction.probability * 100
                print("\t" + prediction.tag_name +
                      ": {0:.2f}%".format(prediction.probability * 100))
                
            else:
                break
        return "Image1: Prediction:",r,"Accuracy:",s,"Image2: Prediction:",q,"Accuracy:",w,"Image3: Prediction:",a,"Accuracy:",b
     
