#!flask/bin/python
################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------
# This file implements the REST layer. It uses flask micro framework for server implementation. Calls from front end reaches 
# here as json and being branched out to each projects. Basic level of validation is also being done in this file. #                                                                                                                                  	       
# -------------------------------------------------------------------------------------------------------------------------------
################################################################################################################################
from flask import Flask, jsonify, request, redirect, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.utils import secure_filename
import os
import shutil
import numpy as np
from search import recommend
import json
import re

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
from tensorflow.python.platform import gfile

app = Flask(__name__, static_url_path="")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

# ==============================================================================================================================
#                                                                                                                              
#  Loading the extracted feature vectors for image retrieval                                                                 
#                                                                          						                                                                                                                                    
# ==============================================================================================================================
imgs_len = len(os.listdir('database/dataset'))
extracted_features = np.zeros((imgs_len, 2048), dtype=np.float32)
with open('saved_features_recom.txt') as f:
    for i, line in enumerate(f):
        extracted_features[i, :] = line.split()
print("loaded extracted_features")


# ==============================================================================================================================
#                                                                                                                              
#  This function is used to do the image search/image retrieval
#                                                                                                                              
# ==============================================================================================================================
@app.route('/imgUpload', methods=['GET', 'POST'])
def upload_img():
    print("image upload")
    result = 'static/result'
    if not os.path.exists(result):
        os.mkdir(result)
    shutil.rmtree(result, ignore_errors=True)

    if request.method == 'POST' or request.method == 'GET':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']
        print('filename:', file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:  # and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            recommend(inputloc, extracted_features)
            if os.path.exists(inputloc):
                os.remove(inputloc)
            image_path = "/result"
            image_list = [os.path.join(image_path, file) for file in os.listdir(result)
                          if not file.startswith('.')]
            tag_list = []
            with open('tag_dict.json', 'r') as f:
                tag_dict = json.load(f)
                for image in image_list:
                    image_id = re.search('.*?(\d+).jpg', image).group(1)
                    try:
                        tag_list.append(tag_dict[f'im{image_id}.jpg'])
                    except:
                        tag_list.append('none')
            images = {
                'image_list': image_list,
                'tag_list': tag_list,
                'tag_set': list(set(tag_list))
            }
            return jsonify(images)


# ==============================================================================================================================
#                                                                                                                              
#                                           Main function                                                        	            #						     									       
#  				                                                                                                
# ==============================================================================================================================
@app.route("/")
def main():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
