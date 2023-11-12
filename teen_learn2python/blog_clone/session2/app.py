from flask import Flask, request,render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("hello_world.html")

@app.route("/var_example")
def var_example():
    number = 200 + 300
    return render_template("var_example.html",var=number)


@app.route("/loop_example")
def loop_example():
    return render_template("loop_example.html",var=['a','b','c',1,2,3])

@app.route("/form_example",methods=["GET","POST"])
def form_example():
    if request.method == "GET":
        return render_template ("form_example.html",my_data="")
    if request.method == "POST":
        data = request.form
        return render_template ("form_example.html",my_data=data["my_data"])
        
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
