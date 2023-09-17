#!/usr/bin/python3
from homework3_dir.linked_list import LinkedList

if __name__ == "__main__":
    my_list = LinkedList(range(1, 11))
    print(my_list)
    my_list.append(11)
    print(my_list)
    print(my_list.find_value(7), my_list.find_value(200))
