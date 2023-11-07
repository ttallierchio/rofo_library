from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello There"


@app.route("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{a+b}"


@app.route("/hello/<string:name>/my_favorite_color_is/<string:color>")
def hello_name(name: str, color: str):
    var1 = request.args["var1"]
    var2 = request.args["var2"]
    return f"Hello There, {name}, my favorite color is also {color}, you also entered var1 as{var1} and var2 as {var2}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
