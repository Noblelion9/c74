Process the Image
==================

In this activity, you will learn to process the image to detect the age.

<img src= "https://s3-whjr-curriculum-uploads.whjr.online/1765ed3b-2e9b-4cc5-971c-ef4bd19278fb.gif" width = "480" height = "320">

Follow the given steps to complete this activity:

1. Process the image

* Open the main.py file.

* Detect the face in the image and store the result in img, bbox variables.

    `img, bbox = detector.findFaces(img, draw=False)`
 
* Check if `bbox` exits.

    `if bbox:`

* Get the X,Y,W,H of bbox in respective variables i.e X, Y, W, H.

    `X = bbox[0]['bbox'][0]`

    `Y = bbox[0]['bbox'][1]`

    `W = bbox[0]['bbox'][2]`

    `H = bbox[0]['bbox'][3]`


* Crop the face out of the image.

    `croppedImg = img[Y:Y+H, X:X+W]`

* Resize the image to 200, 200.

    `resizedImg = [cv2.resize(croppedImg, (200, 200))]`
         
* Append resized image to images array.

    `images.append(resizedImg)`

* Convert ages to np.array.

    `ages = np.array(ages,dtype=np.int64)`

* Convert images to np.array.

    `images = np.array(images)`
    
* Print age array.

    `print("Age",ages)`

* Print images array

    `print(images)`

* Save and run the code to check the output.
