from flask import Flask, request


app = Flask(__name__)


def multiplication(x, y):
    return x * y


@app.route("/")
def index():
    return "Hello World"


@app.route("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{a+b}"


@app.route("/multiply")
def multiply_endpoint():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{multiplication(a,b)}"


@app.route("/squared")
def squared():
    a = int(request.args["a"])

    return f"{multiplication(a,a)}"


@app.route("/hello/<string:name>")
def hello_name(name: str):
    return f"Hello There, {name}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
