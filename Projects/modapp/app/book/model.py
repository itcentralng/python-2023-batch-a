from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all(cls):
        return Book.query.all()
    
    @classmethod
    def create(cls, name, author_id):
        book = cls(name=name, author_id=author_id)
        book.save()
        return book