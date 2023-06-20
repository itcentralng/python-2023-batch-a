from flask import Blueprint, request
from app.author.model import Author
from app.author.schema import AuthorSchema

author = Blueprint('author', __name__, url_prefix='/author')

@author.get('/all')
def get_all_authors():
    authors = Author.get_all()
    return {'message':'Authors retrieved successfully!', 'authors':AuthorSchema(many=True).dump(authors)}

@author.get('/<int:id>')
def get_author(id):
    author = Author.get_by_id(id)
    return {'message':'Author retrieved successfully!', 'author':AuthorSchema().dump(author)}

@author.post('/add')
def add_author():
    name = request.json.get('name')
    Author.create(name)
    return {'message':'Author created successfully!'}