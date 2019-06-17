from flask import Flask
import matplotlib.pyplot as plt, mpld3

# the all-important app variable:
app = Flask(__name__)

@app.route("/")
def index():
    plt.plot([3, 1, 4, 1, 5], 'ks-', mec='w', mew=5, ms=20)
    return mpld3.show()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')