import cv2
import face_recognition
import os
import shutil
import sys

#   to run programe ...
#   python sort.py data_folder_name

data_dir = sys.argv[1]
cache = 'sorted/cache'
imname = 0

os.mkdir('sorted')
os.mkdir('sorted/cache')


for images in os.listdir(data_dir):
    img = cv2.imread(data_dir+'/'+images) 
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(rgb_img)[0]   
    # if cache is empty
    if os.listdir('sorted/cache') == []:
        print("imname = " , imname)
        source_img = os.path.join(data_dir , images )
        sorted_path = os.path.join('sorted' , str(imname) )
        print('\ncache is empty source = ', source_img , 'sorted = ' , sorted_path)
        os.mkdir(sorted_path)
        _ = shutil.copy(source_img , sorted_path)
        _ = shutil.copy(source_img , cache)
        # rename the file as integer in cache 
        os.rename(cache + '/' + images , cache+'/'+str(imname)+'.jpeg' )
        imname = 1 + imname


    # if cash has some images 
    img_cimg_matched = False
    for cached_img in os.listdir(cache):
        cimg = cv2.imread('sorted/cache/'+cached_img)
        rgb_cimg = cv2.cvtColor(cimg, cv2.COLOR_BGR2RGB)
        cimg_encoding = face_recognition.face_encodings(rgb_cimg)[0]
        #if match then copy img to the approriate folder and break
        res = face_recognition.compare_faces([cimg_encoding] , img_encoding )
        if res[0] : 
            print(data_dir+'/'+ images , 'sorted/'+cached_img[:-5])
            # print("cached image and adani matched" , cached_img , images)
            _ = shutil.copy( data_dir+'/'+ images , 'sorted/'+cached_img[:-5] )
            img_cimg_matched = True
            break 
        #else next image


    #if not match in any case then copy file to cache , make new appropriate sorted folder , copy image to that folder , rename image to proper integer for cache

    if not img_cimg_matched :
        source_img = os.path.join(data_dir , images )
        print("imname = " , imname)
        sorted_path = os.path.join('sorted' , str(imname) )
        print('\ncreating file in cache source = ', source_img , 'sorted = ' , sorted_path)
        os.mkdir(sorted_path)
        _ = shutil.copy(source_img , sorted_path)
        _ = shutil.copy(source_img , cache)
        # rename the file as integer in cache 
        os.rename(cache + '/' + images , cache+'/'+str(imname)+'.jpeg' )
        imname = 1 + imname




# addition thins one can do
    # - add log file , so that when the data_dir is modified (added new data) then it would be easy to keep track of already processed images and can process only new data
    # - increase speed by storing all cache images face incoding values to the list and next time comparing data image just have to compare no need to extract face encoding again , it would improve performance !