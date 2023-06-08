from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all(cls):
        return Book.query.all()
    
    @classmethod
    def create(cls, name):
        book = cls(name=name)
        book.save()
        return book