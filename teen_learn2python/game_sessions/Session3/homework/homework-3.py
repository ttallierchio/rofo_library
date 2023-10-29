#!/usr/bin/python3

if __name__ == '__main__':
    
    for x in range(1,251):
        out = ""
        if x % 3 == 0:
            out += "fizz"
        if x % 5 == 0:
            out += "buzz"
        if out:
            print(out)