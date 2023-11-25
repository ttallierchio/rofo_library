# Homework Break Down


## Problem 1

### The problem statement
`Create a template that has a form to show your name from input boxes. So when you click submit, the website should update and show “hello <your name>”`

I built out my application with the following back end code

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

if its a `GET` we wont have data in our form attribute. if its a `POST` we will have data in the form attribute.

this in turn will pass to our template and allow the template to render with a first and last name,or just render the form of the HTML


the below is the template code.
```jinja
<HTML>
    <BODY>
        <DIV>
            {% if first_name != "" %}
                <p>Hello {{ first_name + ' ' + last_name }}
            {% endif %}
            <FORM method="POST">
                <label class="color_text">first name:</label><input name="first_name" type="textbox"><br>
                <label class="color_text">last name:</label><input name="last_name" type="textbox"><br>
                <INPUT type=submit>
            </FORM>
    </DIV>

    </BODY>
</HTML>
```

we use an if statement to show if first name exists, if it does we then put an additional `<p>` element on the page and write out first name and last name, this is done in the pre rendering part of the template before we send it to the browser that requested it.

## Problem 2
### The problem statement
`Create a template with a link to another webpage. Can be a template, or something as simple as google.com`

I have provided both examples, we link to the original template we have built, as well as `www.google.com`

```html
<html>
    <body>
        <a href="http://www.google.com"> go to google</a>
        <a href= "/load_template_1">load your other template!
</body>
</HTML>
```
as you can see we have two `<a>` links and one says go to google, the other load your other template. 

the python code behind the scenes looks like this
```python
from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("template2.html")

@app.route("/load_template_1",methods=["GET","POST"])
def another_page():
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
we have to use the same logic to fill in the first and last name, as we are loading a new app essentially.

## Problem 3

### The problem statement
`Create a template that uses a loop to print out 1 to 100.`

This code is done all in the template. did you know you can run almost all of the same built-in python functions in the template you can in your back end code? 

```jinja
<html>
    <body>
        <ul>
{% for n in range(1,101) %}
<li>{{n}}</li>

{% endfor %}
        </ul>
    </body>
    </html>
```

this creates a loop and renders 1 to 100 on the page thats it
the python code for the app
```python
from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("template3.html")
```
## Problem 4
### The problem statement
`Create a template that changes its font color based on a query string parameter`

this is very similar to the first problem except we are using the query string to pass in a value and not form data. that means we only need to use the `GET` method.

```python
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = request.args
    if "color" in data:
        color = data["color"]
    else:
        color = "blue"
    return render_template("template4.html", color=color)
```

we are checking to see if color exists in the query string, and if not we are replacing it with blue. 

```jinja
<HTML>

    <HEAD>
        <style>
            .color_text {
                color: {{ color }}
            }
        </style>
    </HEAD>
    <body><div class="color_text">look at this text</div></body></html>
```

here we are defining a class with the color we pass in. in the `<style>` blocks we are saying make a custom class called `color_text`. anything with a `.` in front of it in the style block is a custom class. we are then saying for `color` set it to what ever the color is passed from the web server. in this case its whatever you set for the query string.
