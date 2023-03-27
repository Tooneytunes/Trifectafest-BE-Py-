from flask import Flask
import rahul
import andu
import toon
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/rahul")
def rahul1():
    return rahul.functie1()

@app.route("/andu")
def andu1():
    return andu.functie2()

@app.route("/toon")
def toon1():
    return toon.functie3()