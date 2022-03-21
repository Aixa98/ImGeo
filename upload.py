# Importamos todo lo necesario

import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
from PIL import Image
# instancia del objeto Flask
app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './Archivos tiff, tfw'


@app.route("/")
def upload_file():
    # renderiamos la plantilla "upload-img.html"
    return render_template('upload-img.html')


@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos tiff"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Retornamos una respuesta satisfactoria
        return "<h1>Archivo subido exitosamente</h1>"


im = Image.open("/C:/Users/Usuario/Documents/images/filled.tiff")
print("Dimensions : {}".format(im.size))
for id in im.tag:
    print("{} : {}".format(id, im.tag[id]))

if __name__ == '__main__':
    # Iniciamos la aplicación
    app.run(debug=True, port=8000)
