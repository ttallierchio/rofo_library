if __name__ == '__main__':
    
    list_example = [1,2,3,4,5,6,7,8,9,10]
    list_of_strings = ["i","am","a","list","of","strings"]
    list_of_lists = [list_example,list_of_strings]
    
    print(list_example)
    print(list_of_strings)
    print(list_of_lists)



    list_sample = [1,2]
    
    list_sample.append(3)
    list_sample = list_sample + [4]
    list_sample += [5]
    print(list_sample)
    list_sample.remove(5)
    print(list_sample.index(4))
    print(list_sample[0])
    
    
    unboxing_sample = [1,2,3]
    
    val_1,val_2,val_3 = unboxing_sample
    print(val_1)
    
    
    
    for_loop_ex = [2,4,6,8,10]
    for num in for_loop_ex:
        print(num)
    
    for num in range(0,11,2):
        print(num)