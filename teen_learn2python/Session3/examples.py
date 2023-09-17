#!/usr/bin/python3
if __name__ == "__main__":
    list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_of_strings = ["i", "am", "a", "list", "of", "strings"]
    list_of_lists = [list_example, list_of_strings]

    print(list_example)
    print(len(list_example))
    print(list_of_strings)
    print(list_of_lists)

    list_sample = [1, 2]

    list_sample.append(3)
    list_sample = list_sample + [4]
    list_sample += [5]
    print(list_sample)
    list_sample.remove(5)
    print(list_sample.index(4))
    print(list_sample[0])

    unboxing_sample = [1, 2, 3]

    val_1, val_2, val_3 = unboxing_sample
    print(val_1)

    for_loop_ex = [2, 4, 6, 8, 10]
    for num in for_loop_ex:
        print(num)

    for num in range(0, 11, 2):
        print(num)
        
    for num in range(0,11):
        if num == 5:
            continue
        print(num)

    for num in range(0,11):
        if num == 7:
            break
        print(num)




do_something = True
while do_something:
    print("we did it")
    do_something = False

count = 0
while count < 50:
    count = count + 1
    print(count)
    
    
dict_example = {"value_int":100,"value_str":"value_str","value_list":[1,2,3,4,5,6]}
print(dict_example)
print(dict_example.keys())
print(dict_example.values())
print(dict_example.items())
print(dict_example["value_list"])


data = range(1,21)

evens = [x for x in data if x % 2 == 0]
odds = [x for x in data if x % 2 == 1]
print(evens,odds)

#zip combines same size lists into seperate tuples, so in this case its 2,1 - 4,3 - 6,5
new_dict = {x:y for x,y in zip(evens,odds)}
print(new_dict)