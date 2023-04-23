import cv2
import face_recognition
import os
import shutil
import sys

path_data = "data"
path_sorted = "sorted"

faces = []

for data_image in os.listdir(path_data):
    dimg = cv2.imread(path_data+data_image)
    rgb_img = cv2.cvtColor(dimg, cv2.COLOR_BGR2RGB)
    dimg_encoding = face_recognition.face_encodings(rgb_img)[0]

    if dimg_encoding not in faces:
        faces.append(dimg_encoding)
        os.mkdir(path_sorted+str(len(faces)))
        # move image to new folder 
    
    else:
        # move image to folder of index where its located 
