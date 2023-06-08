from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost/libraryapp"

# create the extension
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

@app.get('/')
def index():
    return "App running successfully!"

from app.book.route import book
app.register_blueprint(book)
from app.author.route import author
app.register_blueprint(author)