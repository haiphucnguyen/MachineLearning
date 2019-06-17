from flask import Flask, request, jsonify, send_file, Response
from werkzeug.utils import secure_filename
import os
import io
import numpy as np
import matplotlib.pyplot as plt, mpld3
import matplotlib.image as mpimg

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

    fig = plt.figure()
    img = mpimg.imread(file)
    plt.imshow(img)

    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route("/detect")
def detectObject():
    x = np.arange(0, 2 * np.pi, 0.01)
    s = np.cos(x) ** 2
    plt.plot(x, s)

    plt.xlabel('xlabel(X)')
    plt.ylabel('ylabel(Y)')
    plt.title('Simple Graph!')
    plt.grid(True)

    return jsonify([mpld3.fig_to_html(plt.figure())])

@app.route('/plot')
def plot():
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1)
    x = np.arange(0, 2 * np.pi, 0.01)
    s = np.cos(x) ** 2
    axis.plot(x, s)

    plt.xlabel('xlabel(X)')
    plt.ylabel('ylabel(Y)')
    plt.title('Simple Graph!')
    plt.grid(True)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')