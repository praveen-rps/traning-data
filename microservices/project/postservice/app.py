from flask import Flask, request, jsonify
from models import db, Post
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microproject.db'
db.init_app(app)

@app.before_request
def create_table():
    db.create_all()

@app.route("/posts/getcomments/<int:postid>")
def getCommentsforPostId(postid):
    data = requests.get(f"http://localhost:5002/comments/postid/{postid}")
    #return jsonify([{'commenter':d.commenter, 'comment':d.comment, 'postid':d.postid} for d in data ])
    return data.json(), 200

@app.route('/posts', methods=['POST'])
def add_post():
    post = request.json
    new_post = Post(postid=post['postid'], author = post['author'], title = post['title'],
                    description = post['description'])

    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message':'Post added'}), 201


@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'postid': p.postid, 'author':p.author, 'title':p.title, 'description':p.description} for p in posts ])


if __name__ == '__main__':
    app.run(port=5001)