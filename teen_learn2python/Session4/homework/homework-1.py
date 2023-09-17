def my_function(prompt_str: str = "give me input! "):
    return input(prompt_str)


if __name__ == "__main__":
    print(my_function())
    print(my_function("not the same input "))
