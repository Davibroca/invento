import os
import glob
import cv2
from bing_image_downloader import downloader
query_string = input("Input Query")
dir = 'dataset'
downloader.download(query_string, limit=10,  output_dir= dir)
loc = os.getcwd()
#path = os.path.join(loc,dir)
path = loc + '/dataset/' + query_string
os.chdir(path)
path = path + '/*'
file = glob.glob(path)
num=1
for f in file:
    img = cv2.imread(f)
    resized = cv2.resize(img,(1280,720))
    name = 'img_' + str(num)
    num+=1
    cv2.imwrite(name + '.jpg',resized)
    os.remove(f)