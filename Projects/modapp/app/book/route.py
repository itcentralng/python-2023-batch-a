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
    Book.create(name)
    return {'message':'Book created successfully!'}