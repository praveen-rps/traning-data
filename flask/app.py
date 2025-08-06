from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/welcome/<name>/<city>")
def greeting(name,city):
    return render_template('welcome.html', sname=name, scity=city)

@app.route("/")
def home():
    return "Welcome to Flask Programming"

@app.route("/test")
def home1():
    return "Welcome to Flask Programming -Test url is called"

if __name__ == '__main__':
    app.run(debug=True)
