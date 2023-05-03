import cv2
import face_recognition
import os
import shutil
import sys

path_data = "./data/"
path_sorted = "./sorted/"
new_image_number = 0
tf = False
faces = []

for data_image in os.listdir(path_data):
    dimg = cv2.imread(path_data+data_image)
    rgb_img = cv2.cvtColor(dimg, cv2.COLOR_BGR2RGB)
    dimg_encoding = face_recognition.face_encodings(rgb_img)[0]

    res = face_recognition.compare_faces(faces , dimg_encoding )  
    print(res)
    #  if no mathes found and the image contain new face
    if not any(res):
        new_image_number = str(len(faces))
        faces.append(dimg_encoding)
        os.mkdir(path_sorted+new_image_number)
        # move image to new folder 
        shutil.copy(path_data+data_image , path_sorted+new_image_number )
    
    else:
        # move image to folder of index where its located 
        new_image_number = str(res.index(True))
        shutil.copy(path_data+data_image , path_sorted+new_image_number )


