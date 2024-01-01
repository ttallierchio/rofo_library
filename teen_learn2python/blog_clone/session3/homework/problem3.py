from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("homework_three.html")


@app.route("/is_even/<int:number>")
def is_even(number: int):
    return {"value": "yes"} if number % 2 == 0 else {"value": "no"}
