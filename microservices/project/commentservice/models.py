from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comment(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    commenter = db.Column(db.String(30), nullable=False)
    comment = db.Column(db.String(50), nullable=False)
    postid = db.Column(db.Integer, primary_key=True)