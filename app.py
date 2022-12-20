# I will be using Werkzeug which will allow the webapp to send and receive cookies, generating 
# sessions, and generating redirects. It will essentially make the webapp more secure.

from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from main import getPrediction
import os

# First, we will save uploaded images to the 'static/uploaded_images' folder.
UPLOAD_FOLDER = 'static/uploaded_images/'

# Create an application object using the Flask class
app = Flask(__name__, static_folder='static')

# We can now add reference fingerprints.
# Cookies will be encrypted using a secret key, to forbid users to change the cookie.
app.secret_key = 'ultra secret key'

# Defining the folder were uploaded image files will be saved.
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  

# Defining the route to home directory.
# index.html is within the home directory, hence our need to define the route home.
@app.route('/')
def index():
    return render_template('index.html')

# Adding a a POST method to th decorator in order to allow form submission.

@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not  in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '': # If user hits submit without selecting a file, the following will be executed.
            flash('No image selected for uploading')
            return redirect(request.url)
        if file: # If we have the file, get the file name and encrypt it using the werkzeug method.
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # Save the file to the upload folder.
            label = getPrediction(filename) # Running the Deep Learning Prediction Model
            flash(label) # Flashing the prediction result.
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            flash(full_filename)
            return redirect('/')

# Running the application.
if __name__ == '__main__':
    app.run()