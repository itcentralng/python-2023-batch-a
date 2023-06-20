from flask import Blueprint, request

from app.book.model import Book
from app.book.schema import BookSchema

book = Blueprint('book', __name__, url_prefix='/book')

@book.get('/all')
def get_all_books():
    books = Book.get_all()
    return {'message':'Books retrived successfully!', 'books':BookSchema(many=True).dump(books)}

@book.post('/add')
def add_new_book():
    name = request.json.get('name')
    author_id = request.json.get('author_id')
    Book.create(name, author_id)
    return {'message':'Book created successfully!'}