from flask import Flask, request
from werkzeug.utils import secure_filename
import os

# the all-important app variable:
app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def uploadFiles():
    images = request.files.to_dict()
    print(images)
    for image in images:
        file = images[image]
        file_name = secure_filename(file.filename)
        file.save(os.path.join('upload', file_name))

    return "Successfully"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')