from flask import Flask, request, render_template
from random import randint
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("homework_two.html")

@app.route("/car")
def car():
    return {"make":"honda","model":"civic","color":"black","year":2023}
