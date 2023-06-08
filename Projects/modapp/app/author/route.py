from flask import Blueprint

author = Blueprint('author', __name__, url_prefix='/author')

@author.get('/all')
def get_all_authors():
    return {'message':'Authors retrieved successfully!', 'authors':[]}