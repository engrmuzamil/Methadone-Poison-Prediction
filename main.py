from flask import Flask, render_template, request
from model import check_file
import os
a = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'static/files'
a.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@a.route("/")
def home():
    return render_template("index.html", pred="a")

@a.route("/result", methods = ['POST'])
def result():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
           file_path = os.path.join(a.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           predection = check_file(file_path)
           return render_template("index.html", pred=predection)
    else:
        return render_template("index.html", pred = "a")
if __name__ == '__main__':
    a.run(debug=True)