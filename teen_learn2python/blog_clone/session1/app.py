from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello There"


@app.route("/add")
def add():
    a = int(request.args)
    b = int(request.args["b"])
    return f"{a+b}"


@app.route("/hello/<string:name>")
def hello_name(name: str):
    return f"Hello There, {name}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
