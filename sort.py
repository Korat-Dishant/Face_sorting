import cv2
import face_recognition
import os
import shutil
import sys

path_data = "data/"
path_sorted = "sorted/"
new_image_number = 0
tf = False
faces = []

for data_image in os.listdir(path_data):
    dimg = cv2.imread(path_data+data_image)
    rgb_img = cv2.cvtColor(dimg, cv2.COLOR_BGR2RGB)
    dimg_encoding = face_recognition.face_encodings(rgb_img)[0]

    for i in faces:
        if i == dimg_encoding :
            tf = True
    print(tf, "for image = ", data_image)
    faces.append(dimg_encoding)
  
    # if not tf:
    #     faces.append(dimg_encoding)
    #     new_image_number = str(len(faces))
    #     os.mkdir(path_sorted+new_image_number)
    #     # move image to new folder 
    #     shutil.copy(path_data+data_image , path_sorted+new_image_number )
    
    # else:
    #     # move image to folder of index where its located 
    #     shutil.copy(path_data+data_image , path_sorted+new_image_number )

