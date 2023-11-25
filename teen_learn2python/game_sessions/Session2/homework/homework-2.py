#!/usr/bin/python3

if __name__ == "__main__":
    input_grade = input("enter the grade ")

    if input_grade.isnumeric():
        data = int(input_grade)
        if data >= 90 and data <= 100:
            print("Excellent!")
        elif data >= 80 and data <= 89:
            print("Great!")
        elif data >= 70 and data <= 79:
            print("Average")
        elif data >= 60 and data <= 69:
            print("You can do better")
        elif data >= 0 and data <= 59:
            print("You failed!")
        else:
            print("Please enter a valid grade 0-100, A-F")
    else:
        if input_grade == "A":
            print("Excellent!")
        elif input_grade == "B":
            print("Great!")
        elif input_grade == "C":
            print("Average")
        elif input_grade == "D":
            print("You can do better")
        elif input_grade == "F":
            print("You failed!")
        else:
            print("Please enter a valid grade 0-100, A-F")
