from datetime import datetime

from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import requests
from flask import request

from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Book(db.Model):
    id: int
    title: str
    image: str
    isbn: str
    auth: str
    publisher: str
    status: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))
    isbn = db.Column(db.String(200))
    auth = db.Column(db.String(200))
    publisher = db.Column(db.String(300))
    status = db.Column(db.Integer)


@dataclass
class BookUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    UniqueConstraint('user_id', 'book_id', name='user_book_unique')


@dataclass
class Wishlists(db.Model):
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/api/books', methods=['GET'])
@app.route('/api/books/<int:page>')
def index(page=None):
    if page is None:
        page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    if request.args.get('search') is None:
        record_query = Book.query.paginate(page, per_page, False)
    else:
        search = "%{}%".format(request.args.get('search'))
        record_query = Book.query.filter(
                                    (Book.title.like(search)) |
                                    (Book.auth.like(search)) |
                                    (Book.publisher.like(search)) |
                                    (Book.isbn.like(search))
                                    ).paginate(page, per_page, False)

    data = {
             "books": record_query.items,
             "total": record_query.total,
             "next": record_query.has_next,
            }
    return jsonify(data)


@app.route('/api/wishlist', methods=['POST'])
def wishlist():
    request_data = request.get_json()

    book_id = request_data['id']
    quantity = request_data['quantity']

    req = requests.get('http://docker.for.mac.localhost:8000/api/user')
    json = req.json()
    user_id = json['id']

    try:
        #wishlists = Wishlists(book_id=book_id, quantity=quantity, user_id=user_id)
        #db.session.add(wishlists)
        #db.session.commit()
        data = {
            "book_id": book_id,
            "quantity": quantity,
            "user_id": user_id
        }
        publish('book_to_wishlist', data)

    except Exception as e:
        abort(400, 'You already add to wishlist this product')

    return jsonify({
        'message': 'success'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
