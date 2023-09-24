Store Age, Gender and Labels
=============================

In this activity, you will learn to store the age, gender and lables in an array.

<img src= "https://s3-whjr-curriculum-uploads.whjr.online/666e8437-72ad-4116-8f94-7d2a4c184614.gif" width = "480" height = "320">

Follow the given steps to complete this activity:

1. Store age, gender and labels

* Open the main.py file.

* Check if `img` is not equal to `.git` i.e a wrong format image.

    `if img!='.git':`

* Split the label to store the age for each image using `.split()` to get the age from the image path.

    `age = img.split("_")[0]`

* Split the label to store the gender for each image using `.split()`to get the gender from the image path.

    `genders = img.split("_")[1]`

* Read the image.
            
    `img = cv2.imread(str(path)+"/"+str(img))`       

* Convert image from BGR to RGB format.
            
    `img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)`
            

* Append the age in ages array.

    `ages.append(age)`

* Store the ages in the numpy array.

    `ages = np.array(ages,dtype=np.int64)`

* Save and run the code to check the output.
