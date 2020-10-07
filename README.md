# Pets prediction with ImageAI

For README in Bulgarian [click here](https://github.com/SimetoB/pets-prediction-with-imageai/blob/master/README.bg.md).

This is my project for university subject "Introduction to Neural Network with Python". A simple image prediction program using ImageAI library.

[Click here](https://github.com/OlafenwaMoses/ImageAI) to check their Github page.

### Dependencies

* Python 3.7.9
* Tensorflow 1.15.2
* OpenCV
* Keras 2.x

### Installation

Install dependencies of ImageAI:

```
pip install tensorflow==1.15.2 keras opencv-python
```
Install ImageAI:

```
pip3 install imageai
```

### Usage

model-training.py is the script that we'll be using to train a model of the pets/animals that we want our program to predict. It uses the same custom image prediction algorithm as the guide [here](https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Prediction/CUSTOMTRAINING.md#custom-model-training). The changes I've made:
1. num_objects has been set to 3 as that's the amount we have in the example.
2. num_experiments has been set to 15, that's how much images for training we have from each pet/animal.
3. batch_size has been set to 5 to balance the load.
4. show_network_summary has been set to False so it doesn't fill the console with noise.

main.py is the script that will run image predictions on every image that is present in folder "images-to-predict". It uses the template from ImageAI for image prediction, which can be found [here](https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Prediction/CUSTOMPREDICTION.md#firstcustompredictionpy). The thing I've changed here are:
1. Model path has been changed to match our custom model created with model-training.py.
2. Instead of running image prediction only on 1 file, I've added a for loop to iterate over every image in the folder "images-to-predict". It uses the os.walk function.
3. Since we're running image prediction on multiple files, I've changed the print statement to output the name of the file and the top prediction for that image.

The current state of the project has one major flaw and that's the lack of a good trained model. As per ImageAI's recommendation, the custom model trainer should have at least 500 images per object and 100 images per object to run tests and train the model. Due to this at the moment most of the image predicting results are cat as top prediction, but with proper training it should perform the work it's intended to.
