from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/welcome/<str:n1>/<str:n2>")
def greeting(n1,n2):
    sum = n1+n2
    return render_template('welcome.html', n1=n1,n2=n2,sum=sum)

@app.route("/")
def home():
    return "Welcome to Flask Programming"

@app.route("/test")
def home1():
    return "Welcome to Flask Programming -Test url is called"

if __name__ == '__main__':
    app.run(debug=True)
