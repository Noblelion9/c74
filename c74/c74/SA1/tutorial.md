Feed the Labeled Images
=======================

In this activity, you will learn to feed the labeled images to the model to make prediction.

<img src= "https://s3-whjr-curriculum-uploads.whjr.online/62c01293-0e0f-428e-8623-3d96cbd04d64.gif" width = "480" height = "320">

Follow the given steps to complete this activity:

1. Download and label the images

* Open the main.py file.

* Download the images.

* Move the downloaded images to `Face-image-dataset` folder.

* Create a path variable that holds relative address to the dataset folder.

    `path = "Face-image-dataset-small"`

* Label the images 0,1 and 2 in the format `Age-Gender( 0 for Male and 1 for Female)-Image number-.jpg.chip.jpg`

    `1_0_0_20161219154909149.jpg.chip`

    `10_0_0_20170110225557604.jpg.chip`

    `101_1_2_20170105174739309.jpg.chip`

* Go through each image i.e img in the variable path using a for loop.

    `for img in os.listdir(path):`

* Write a try except block.

    `try:`

    `except:`

        `print("Error in reading")`

* Print the `img` in the try block.
    
    `print(img)`

    
* Save and run the code to check the output.
