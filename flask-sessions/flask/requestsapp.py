from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template('login.html')

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        return "POST Method is called from the browser!"
    else:
        return "Get Method is called from the browser"

@app.route("/get", methods=['GET'])
def home1():
    return "Get Method is called..!"

@app.route("/post", methods=['POST'])
def home2():
    return "Post Method is called..!"

@app.route("/delete", methods=['DELETE'])
def home3():
    return "Delete Method is called..!"

@app.route("/put", methods=['PUT'])
def home4():
    return "Put Method is called..!"

if __name__ == '__main__':
    app.run(debug=True)