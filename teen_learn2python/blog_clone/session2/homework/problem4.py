from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/")

def index():
    data = request.args
    if "color" in data:
        color = data["color"]
    else:
        color = "blue"
    return render_template("template4.html",color=color)