from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def index():
    return "Hello this is an app created with flask"

@app.get('/welcome')
def welcome_page():
    return "Hello, Welcome to our first page with flask"

@app.get('/html')
def return_html():
    name = "Aisha"
    age = 16
    friends = [
        {"name":"Jamil Salis", "age":22, "picture":"user1.jpg"},
        {"name":"Abubakar Galadima", "age":12, "picture":"user2.jpg"},
        {"name":"Zainab Garba", "age":12},
    ]
    return render_template('index.html', age=age, name=name, friends=friends)

if __name__ == "__main__":
    app.run(debug=True)