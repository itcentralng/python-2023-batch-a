from flask import Flask,request,session
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import generate_password_hash as gph, check_password_hash as cph


# create the extension
db = SQLAlchemy()

app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

app.secret_key = "ijhdiguihdsojhuidsgid"

# initialize the app with the extension
db.init_app(app)


#welcome
@app.get('/')
def welcome():
    return "welcome to my Library"


#create a book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.String)
    publisher = db.Column(db.String)
    content = db.Column(db.String)

#create Model for admin
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

with app.app_context():
    db.create_all()

def authenticate(username, password):
    #admin = Admin.query.filter_by(username=username).first()
    user = "admin"
    #pass = "password"

    if user==username:
        return user

def identity(payload):
    admin_id = payload['identity']
    return Admin.query.filter_by(id=admin_id).first()

jwt = JWT(app, authenticate, identity)


#create post 
@app.post('/add_book')
def add_book():

    name = request.json.get('name')
    author = request.json.get('author')
    publisher = request.json.get('publisher')
    content = request.json.get('content')

    new_book = Book(name=name, author=author, publisher=publisher, content=content)
    db.session.add(new_book)
    db.session.commit()
    return "new_book added successfully"


@app.get('/get_book')
def get_book():
    books= Book.query.all()
    books = [{'id':book.id, 'name': book.name, 'author': book.author, 'publisher': book.publisher, 'content': book.content} for book in books]
    return {'books': books}



@app.put('/update_book')
def update_book():
    name= request.json.get('name')
    author = request.json.get('author')
    publisher = request.json.get('publisher')

    book= Book.query.filter_by(id=id).first()

    book.name= name or book.name
    book.author= author or book.author
    book.publisher= publisher or book.publilsher

    db.session.commit()
    return "book updated successfully"




@app.post('/login') 
def login():
    password = request.json.get('password')
    email = request.json.get("email")  



if __name__ == "__main__":
     app.run(debug=True)