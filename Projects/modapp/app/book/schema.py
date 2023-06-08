from app import ma
from app.book.model import Book

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book