# Homework Break Down


## Problem 1

`Create a template that has a form to show your name from input boxes. So when you click submit, the website should update and show “hello <your name>”`

i built out my application with the following back end code

```python
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
```
    This index page has two methods a `GET` and a `POST`. these two methods allow me to do everything in one end point based on what the browser sends me. 
    remeber make python do the work for you.

    if its a `GET` we wont have data in our form attribute. 
## Problem 2

## Problem 3

## Problem 4
