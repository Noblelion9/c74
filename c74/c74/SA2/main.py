import numpy as np
import os
import cv2
from cvzone.FaceDetectionModule import FaceDetector

path = "C:/Users/arnav/Downloads/c74/c74/SA2/Face-image-dataset-small"
images=[]
ages=[]



detector = FaceDetector()

for img in os.listdir(path):
    try:
        print(img)

        # Check if img is not equal to .git i.e a wrong format image 
        if img!='.git':
            age = img.split("_")[0]
            # Get the age from the image path i.e img

            #Append age to ages array
            ages.append(age)
            # Read the image
            img = cv2.imread(str(path)+"/"+str(img))
            # Convert image from BGR to RGB format
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Display the age on the image
            img = cv2.putText(img, "Age= " +age,(60, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0 ,255), 1)
    except:
        print("error in reading")

# Convert ages to np.array
ages = np.array(ages, dtype=np.int64)
# Print ages
print("Age", ages)