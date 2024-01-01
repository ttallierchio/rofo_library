from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("homework_one.html")
