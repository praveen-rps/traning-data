from flask import Flask, request, jsonify
from models import db, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microproject.db'
db.init_app(app)

@app.before_request
def create_table():
    db.create_all()

@app.route('/comments', methods=['POST'])
def add_comment():
    comment1 = request.json
    new_comment = Comment(cid=comment1['cid'],  commenter = comment1['commenter'], comment = comment1['comment'],
                    postid = comment1['postid'])

    db.session.add(new_comment)
    db.session.commit()
    return jsonify({'message':'Comment added'}), 201

#http://localhost:5002/comments/postid/1001
@app.route("/comments/postid/<int:pid>")
def get_comments_for_postId(pid):
    print("Inside the comments servie")
    data = Comment.query.filter_by(postid=pid).all()
    result = []
    for d in data:
        result.append({
            "cid":d.cid,
            "comment":d.comment,
            "commenter":d.commenter,
            "postid":d.postid
        })
    return jsonify(result),200

@app.route('/comments', methods=['GET'])
def get_posts():
    comments = Comment.query.all()
    return jsonify([{'cid': c.cid, 'commenter':c.commenter, 'comment':c.comment, 'postid':c.postid} for c in comments ])


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5002)

