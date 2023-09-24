import numpy as np
import os
import cv2
from cvzone.FaceDetectionModule import FaceDetector

'''
LABLE THE IMAGES 0-6 AS FOLLOWS:

0: 1_0_0_20170110213104570.jpg.chip
1: 8_1_2_20170109205348937.jpg.chip
2: 11_1_0_20170109203353740.jpg.chip
3: 14_0_0_20170103200615511.jpg.chip
4: 15_0_4_20170103201013615.jpg.chip
5: 24_0_1_20170116000614713.jpg.chip
6: 27_0_4_20170103235757172.jpg.chip
'''

path = "Face-image-dataset-small"
images = []
ages = []

detector = FaceDetector()

for img in os.listdir(path):
    try:
        print(img)
        if img!='.git':
            age = img.split("_")[0]
            genders = img.split("_")[1]
            img = cv2.imread(str(path)+"/"+str(img))
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            
            img, bbox = detector.findFaces(img, draw=False) 
 
            if bbox:
                X = bbox[0]['bbox'][0]
                Y = bbox[0]['bbox'][1]
                W = bbox[0]['bbox'][2]
                H = bbox[0]['bbox'][3]

                croppedImg = img[Y:Y+H, X:X+W]
                resizedImg = [cv2.resize(croppedImg, (200, 200))]
                      
                images.append(resizedImg)
                
                ages.append(age)
    except:
        print("error in reading")

ages = np.array(ages,dtype=np.int64)

images = np.array(images)

print("Age",ages)
print(images)