from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Programming"

@app.route("/test")
def home1():
    return "Welcome to Flask Programming -Test url is called"

if __name__ == '__main__':
    app.run(debug=True)
