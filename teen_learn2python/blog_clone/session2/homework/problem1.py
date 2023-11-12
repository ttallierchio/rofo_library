from flask import Flask, request,render_template

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    data = request.form

    if "first_name" in data:
        first_name = data["first_name"]
    else:
        first_name = ""
    
    if "last_name" in data:
        last_name = data["last_name"]
    else:
        last_name = ""
    return render_template("template1.html",first_name=first_name,last_name=last_name)
