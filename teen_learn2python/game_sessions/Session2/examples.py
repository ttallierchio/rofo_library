int_val_1 = 1
int_val_2 = 2
string_val_1 = "foo"
string_val_2 = "bar"

if int_val_1 == 1:
    print("true")

if int_val_2 != 1:
    print("true")

if int_val_1 < int_val_2:
    print("true")

if int_val_2 >= int_val_1:
    print("true")

if int_val_1 <= int_val_2:
    print("true")
if string_val_1 != string_val_2:
    print("true")

if string_val_1 != "foo":
    print("true")

if "abc" == "abc":
    print("basic if statement")

if "abc" != "abc":
    print("wont print")
elif "abc" == "abc":
    print("will print the else if")

if "im wont match" == "sure wont match":
    print("wont print")
else:
    print("will print with the else")


str_val_true = "test"
none_val = None
str_val_false = ""

if str_val_true:
    print("will show this print - str_val_true")

if none_val:
    print("you will not see this")
if str_val_false:
    print("You will not see this")


names = ["bob", "fred", "susan", "jill"]
str_var = "foobar"


if "bob" in names:
    print("found bob")
if "foo" in str_var:
    print("foo was found")

answer = 42
question = "What is the meaning of life?"

if answer == 42 and question == "What is the meaning of life?":
    print("its not really the right question is it?")

thing = "one"
other_thing = "two"

if other_thing == "one" or thing == "one":
    print("we have at least one thing")

if not answer == 42 or not thing == "two":
    print("these are both false")


number_but_a_string = "42"

if number_but_a_string.isnumeric():
    print("im a number")

if other_thing.isalpha():
    print("im a string")