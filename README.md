# Image Classification Deep Learning Project with Flask Front-End
*Felix Gomez-Guillamon Jurado*

**Model Training can be seen on the file 'ImageClassification .ipynb'**

Deep Learning Image Classification model which detects whether a person is happy or sad by giving a percentage of certainty to its prediction. Used several machine learning libraries such as TensorFlow, Keras and OpenCV. Other libraries such as Matplotlib and Numpy were used to display the model’s performance. 

The Model is able to predict whether a person is sad or happy from any image that is uploaded outside the dataset used for training the model.

### Front-End implementation
Flask Front-End implementation can be found on the file 'app.py' and templates folder for the HTML files. 
Some of the functionalities of the Front-End are:
- Using WerkZeug to let the server send cookies to the client and encrypting the cookies using a unique secret key.
- Everytime a user uploads a picture and then clicks 'submit', the server will save the image in the 'static/uploaded_images' directory. This folder will contain the image/s uploaded by the user.
### Steps to run the project
#### Two Options:
##### Google Colab (Using Colab's GPU)
- Install all neccessary dependencies
	- Can be found on the 'requirements.yaml' file
##### Local Computer - Silicon ARM Mac (recommended)
- Download <a href="https://docs.conda.io/en/main/miniconda.html">Miniconda</a>
- Create a new virtual environment with conda using 'requirements.yaml' file
	- Conda env create -f requirements.yaml
- Conda install jupyter (ignore if already installed)
- Create a specific jupyter kernel for the project for the virtual environment
	- python -m ipykernel install --user --name=ImageClassification
- Open Jupyter Lab / Notebook