from flask import Flask

app = Flask(__name__)

@app.route("/")
def firest_flask():
    return "This is my first flask program"

@app.route("/flask_2")
def second_flask():
    return "Python is fun! Let's start coding"

app.run(debug=True)