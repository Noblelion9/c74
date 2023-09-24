Maximize a Dataset
===================

In this activity, you will learn to add a condition to maximize a dataset to 50 images for each age group.

<img src= "https://media.slid.es/uploads/1525749/images/10561955/Images_Dataset.png" width = "480" height = "320">
<img src= "https://media.slid.es/uploads/1525749/images/10561958/Updated_Images.png" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Create array of the images

* Open the main.py file.

* Create empty arrays named `newAges, newImages`.

* Create an array `count` with value `[0] * len(ages)` to get the count.

   `newAges = []`

   `newImages = []`

    `count = [0] * len(ages)`

* Loop throught each index in range of length of ages.

    `for i in range(len(ages)):`

* Check if count at index `ages[i]` is less then `50`.

    `if count[ages[i]] < 50:`

* Appened the ages at `i` to `newAges` at `i`.

    `newAges.append(ages[i])`

* Appened the images at `i` to `newImages` at `i`.

    `newImages.append(images[i])`

* Incrementt the count at index ages[i] by 1.

    `count[ages[i]] = count[ages[i]] + 1`

* Call `printOccurences()` function with `newAges` as parameter to check updated results.

    `printOccurences(newAges)`

* Save and run the code to check the output.
