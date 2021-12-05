# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:55:42 2021

@author: Himjyoti
"""

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid
import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img


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
    # Display the results.
    for prediction in results.predictions:
        
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))

with open(os.path.join (base_image_location, "Test/test_image2.jpg"), "rb") as image_contents:
    results = predictor.classify_image(
        'e7ea3663-53a3-4644-b52a-1b271839d6dc', 'Iteration1', image_contents.read())
   

   
    plt.figure()
    plt.clf()
    plt.imshow(load_img("Images/Test/test_image2.jpg"), cmap = 'Greys')
    plt.xlabel('Image2')
    print('Actual Number= ২\nPrediction of image2:')
    # Display the results.
    for prediction in results.predictions:
        
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))

with open(os.path.join (base_image_location, "Test/test_image3.jpg"), "rb") as image_contents:
    results = predictor.classify_image(
        'e7ea3663-53a3-4644-b52a-1b271839d6dc', 'Iteration1', image_contents.read())
   

   
    plt.figure()
    plt.clf()
    plt.imshow(load_img("Images/Test/test_image3.jpg"), cmap = 'Greys')
    plt.xlabel('Image3')
    print('Actual Number= ৯\nPrediction of Image 3:')
    # Display the results.
    for prediction in results.predictions:
        
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))
        
     
