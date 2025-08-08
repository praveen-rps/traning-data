from flask import Flask, request, jsonify
import requests


app = Flask(__name__)

# declare the urls where servies are runing

POST_SERVICE_URL = "http://localhost:5001"
COMMENT_SERVICE_URL = "http://localhost:5002"


@app.route("/api/posts", methods=['GET','POST'])
def posts():
    if request.method == 'GET':
        response = requests.get(f"{POST_SERVICE_URL}/posts")
    else:
        response = requests.post(f"{POST_SERVICE_URL}/posts", json = request.json)
    return jsonify(response.json()), response.status_code


@app.route("/api/comments", methods=['GET','POST'])
def comments():
    if request.method == 'GET':
        response = requests.get(f"{COMMENT_SERVICE_URL}/comments")
    else:
        response = requests.post(f"{COMMENT_SERVICE_URL}/comments", json = request.json)
    return jsonify(response.json()), response.status_code


if __name__ == '__main__':
    app.run(port=5000)