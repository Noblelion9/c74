import numpy as np
import os
import cv2
from cvzone.FaceDetectionModule import FaceDetector


path = "Face-image-dataset-small"
images = []
ages = []

detector = FaceDetector()


def printOccurences(ages):
    occurrences = {}

    for element in ages:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1

    for element in occurrences:
        print(str(element) +": " + str(occurrences[element]))


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

#print(images)
#print("Age",ages)

print("Ages::::::::::::::::::::::::::::::::")
printOccurences(ages)

# Create arrays newAges, newImages, count(array of zeros euqal to length og ages)


# Loop throught each index in range of length of ages

    # Check if count at index ages[i] is less then 50
    
        # Uppened the ages at i to newAges at i
        
        # Uppened the images at i to newImages at i
        
        # Incrementt the count at index ages[i] by 1
        

print("Updated ages::::::::::::::::::::::::::::::::")

# Call printOccurences() function with newAges to check updated results

