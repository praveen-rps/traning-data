from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)


books = [
    {"isbn":9001,"name":"Java completer", "publisher":"TataMcGraw", "price":850},
     {"isbn":9002,"name":"Python Developer", "publisher":"Orient", "price":300},
      {"isbn":9003,"name":"DevOps in Action", "publisher":"PenMan", "price":290}
]

users = [
    {"id":9001,"name":"kumar agarwal","username":"kumar123", "email":"kumar@gmail.com" },
     {"id":9002,"name":"sunilr","username":"sunilr123", "email":"sunilr@gmail.com" },
      {"id":9003,"name":"mahesh","username":"mahesh123", "email":"mahesh@gmail.com" },
]

@app.route("/users/<int:id>")
@cross_origin(origins="http://localhost:4200")
def getusers(id):
    usr = next((user for user in users if user['id']==id))
    return jsonify(usr),200

@app.route("/books", methods=['GET'])
def getBooks():
    return jsonify(books), 200

@app.route("/books", methods=['POST'])
def addBook():
    book = request.get_json()
    books.append(book)
    return jsonify(book),201

@app.route("/books/<int:isbn>", methods=['DELETE'])
def deleteBook(isbn):
    book = find_book(isbn)
    if not book:
        return jsonify({"Error":"Book with given isbn is not found"}),404
    else:
        books.remove(book)
    return jsonify({"status":"Book deleted"}),200

@app.route("/books/<int:isbn>")
def searchBook(isbn):
    book = find_book(isbn)
    if book is None:
        return jsonify({"Error":"Book with given isbn is not found"}),404
    else:
        return jsonify(book),200
    
@app.route("/books/<int:isbn>", methods=['PUT'])
def updateBook(isbn):
    book = find_book(isbn);
    if not book:
        return jsonify({"Error":"Book with given isbn is not found"}),404
    data = request.get_json()
    book['name']= data.get("name", book['name'])
    book['publisher'] =  data.get("publisher", book['publisher'])
    book['price'] =  data.get("price", book['price'])
    return jsonify(book),200

    

def find_book(isbn):
    return next((book for book in books if book['isbn']==isbn))


if __name__ == "__main__":
    app.run(debug=True)
    CORS(app, origins=["http://localhost:4200"])