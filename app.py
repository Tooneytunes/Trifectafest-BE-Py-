from flask import Flask
import rahul
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/rahul")
def rahul1():
    return rahul.functie1()
