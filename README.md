# Electrothon-3.0-Team-Adway
# Project: Sign Language Recognition Using Deep Learning

## Initial Commit: 
- We are starting this project with a dataset of single images in each label eg. 1, 2, A, etc.
- Also the ppt is blank or it is just the template provided.

## DataSet Creation
- After capturing more images and applying data augmentaion, the total dataset now contains more than 10,000 images
- Images are captured by
  - Vinay
  - Aakansha
- Dataset is available in my google drive [Dataset Link](https://drive.google.com/drive/folders/1yzGNq1mmUdMcQTC1pcI48zcOqbm9j26i?usp=sharing)

## Creating the CNN Model
- Model 1: Using data as preprocessed by the tensorflow.keras.applications.mobilenet.preprocess_input but the model is created by us.
- Model 2: Using the previous model but the data is in greyscale.
- Model 3: Using the already existing very popular mobilenet model from the tensorflow.keras.applications.mobilenet, and tuning it a little bit as per our requirement.

