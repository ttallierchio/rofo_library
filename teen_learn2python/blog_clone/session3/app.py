from flask import Flask, request, render_template
from random import randint
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<html_page>")
def render_them(html_page):
    return render_template(f"{html_page}.html")
@app.route("/random")
def random():
    return {"value":randint(0,200)}
