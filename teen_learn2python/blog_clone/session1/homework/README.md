# Homework Break Down


## Problem 1.
We need to add two new endpoints a multiple endpoint, and a squared endpoint. 

remeber we are treating the query parameters as a variable for later. just as a refresher a variable is a peice of code that allows us to store a value to manipulate it or use later. you can declare variables by simply typing a name and putting a equal sign at the end like so

### Variables refresher
```python
my_str_var = "im a string"
my_int_var = 123
my_decimal_var = 3.141592654
my_list = ['cheese','crackers','pants']
my_dictonary = {'key':'pair','nested':{'key':'pair'}}
 ```
 this code should run as is

 arguments are alot like parameters, and you should validate what kind of variable they are before storing them. we do this with the `int` function. we reterive them with the `request` object and the `args`
### f strings refresher
we are also making heavy use of f strings in these examples. an f string stands for format string, or a way to have a templated string so you do not have to concatonate multiple strings together. this example shows the difference
```python
string_1 = 'my value'
string_2 = 'my other value'
no_f_strings = string_1 + ' ' + string_2
f_strings - f"{string_1} {string_2}"
print(no_f_strings,f_strings)
```

this code should run as is

### function refresher.
 in my example we create a function with two parameters so we can reuse this code. Reusing code is one of the best patterns you can do, why make changes in three spots when you only need to do it in one?

 with that said do not try to force your code to be reusable all the time, it takes time and practice for when to identify it. 

 as a reminder here is how a function is defined in python

 ```python
def my_function(val_1,val_2):
    my_logic = val_1 + val_2
    return my_logic
print(my_function('abc','123'))
 ```

 this code should run as is

 We define a function with the `def` keyword. this stands for define as in we are defining a function called `my_function`.

 we have two parameters `val_1` and `val_2`

 as we indent the code inside to say this is part of the function, we have a single variable where we add these two values together. then we use the `return` key word to pass that value back. in the case of the multiple function we are simply using the `*` operator.


 and for the second endpoint of squared, we are just passing in the same value twice


 ## Problem 2
 very much like the example, we just added on another dynamic route with color. remeber that you need to add another parameter to your endpoint function that matches your dynamic route. in my case its `color`



 ## Problem 3

 We are now combining both of these together to show that it is possible to use both in your route to have your business logic process them. in the example i provide you see that we are just adding more values to the output string.


 ## Problem 4 
 there is no homework for this one as i want you to try and play around with how to validate your inputs, not all inputs are created equally. you cant store strings in a interger as an example, python will do its best but if something is malformed it will fail and give you the flask debugger screen.


 