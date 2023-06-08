from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import generate_password_hash as gph, check_password_hash as cph

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# create the extension
db = SQLAlchemy()

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per day", "5 per hour"],
    storage_uri="memory://",
)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

# initialize the app with the extension
db.init_app(app)

import os

app.secret_key = os.environ.get('SECRET_KEY')


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    school = db.Column(db.String, nullable=False)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    school = db.Column(db.String, nullable=False)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

with app.app_context():
    db.create_all()

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and cph(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()

jwt = JWT(app, authenticate, identity)

@app.post('/register')
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User(username=username, password=gph(password))
    db.session.add(user)
    db.session.commit()
    return "User created successfully"


@app.post('/add-student')
@jwt_required()
def add_student():
    name = request.json.get('name')
    email = request.json.get('email')
    school = request.json.get('school')
    new_student = Student(name=name, email=email, school=school)
    db.session.add(new_student)
    db.session.commit()
    return "Student Added Successful!"

@app.put('/student/<int:id>')
@jwt_required()
def update_student(id):
    name = request.json.get('name')
    email = request.json.get('email')
    school = request.json.get('school')

    student = Student.query.filter_by(id=id).first()
    student.name = name or student.name
    student.email = email or student.email
    student.school = school or student.school

    db.session.commit()
    return "Student updated successfully"

@app.get('/students')
@jwt_required()
def get_students():
    students = Student.query.all()
    students = [{'id':student.id, 'name': student.name, 'email': student.email, 'school': student.school} for student in students]
    return {'students': students}

@app.get('/student/<int:id>')
@jwt_required()
def get_student(id):
    student = Student.query.filter_by(id=id).first()
    if student:
        student = {'id':student.id, 'name': student.name, 'email': student.email, 'school': student.school}
        return {'student': student}
    return {'message': 'Student not found'}, 404

@app.post('/add-teacher')
@jwt_required()
def add_teacher():
    name = request.json.get('name')
    email = request.json.get('email')
    school = request.json.get('school')
    new_teacher = Teacher(name=name, email=email, school=school)
    db.session.add(new_teacher)
    db.session.commit()
    return "Teacher Added Successful!"

@app.get('/teachers')
# @jwt_required()
def get_teachers():
    teachers = Teacher.query.filter_by(school='iT Central').all()
    teachers = [{'id':teacher.id, 'name': teacher.name, 'email': teacher.email, 'school': teacher.school} for teacher in teachers]
    return {'teachers': teachers}

@app.get('/teacher/<int:id>')
@jwt_required()
def get_teacher(id):
    # Aisha's Code
    # id = request.json.get('id')
    # name = request.json.get('name')
    # email = request.json.get('email')

    # Zainab's Code

    # Halima's Code
    teacher = Teacher.query.filter_by(id=id).first()
    if teacher:
        # Jamilu's Code
        teacher = {"name":teacher.name, "email":teacher.email, "school":teacher.school}
        return {"teacher":teacher}
    return "Teacher not found", 404

@app.put('/teacher/<int:id>')
@jwt_required()
def update_teacher(id):
    name = request.json.get('name')
    email = request.json.get('email')
    school = request.json.get('school')

    teacher = Teacher.query.filter_by(id=id).first()
    teacher.name = name or teacher.name
    teacher.email = email or teacher.email
    teacher.school = school or teacher.school

    db.session.commit()
    return "Teacher updated successfully"

@app.delete('/teacher/<int:id>')
@jwt_required()
def delete_teacher(id):
    Teacher.query.filter_by(id=id).delete()
    db.session.commit()
    return "Teacher deleted successfully"



if __name__ == '__main__':
    app.run(debug=True)