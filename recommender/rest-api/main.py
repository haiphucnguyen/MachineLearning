from flask import Flask

# the all-important app variable:
app = Flask(__name__)

@app.route("/users")
def hello():
    return "Oh, Hello World"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')