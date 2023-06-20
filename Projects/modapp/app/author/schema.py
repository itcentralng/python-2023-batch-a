from app import ma
from app.author.model import Author

class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
    books = ma.Nested('BookSchema', many=True)