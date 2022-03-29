import os
from flask import Flask, jsonify, render_template, request
from werkzeug import secure_filename
from PIL import Image
import csv
import json
import pandas as pd

f = open('upload-img.html')

UPLOAD_FOLDER = 'imgeo-master/uploads'
# instance of the Flask object
app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('imgeo/upload-img.html')
def viewer():
    """Show a map to view the GeoJSON returned from a ImGeo endpoint"""
    return render_template('imgeo/imgeo-master/templates/viewer.html')


@app.route("archivo.json", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # we get the file from the "file" input
        f = request.files['archivo']
        filename = pd.DataFrame(f.filename)
        # Save the file in the directory "tiff files".
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # return "<h1>File uploaded successfully</h1>"


with open("archivo.json", "w") as archivo:
    archivo.write("")
    archivo.close()
pasarlo = pd.DataFrame(pd.read_csv(
    "Greater_London_Const_Region.csv", sep=",", header=0, index_col=False))
pasarlo.to_json("archivo.json", orient="records", date_format="epoch",
                double_precision=10, force_ascii=True, date_unit="ms", default_handler=None)
print(pasarlo)


data = {}


if __name__ == '__main__':
    # Start the application
    app.run(debug=True)

f.write()
f.close()
