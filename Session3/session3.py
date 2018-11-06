def fib_list(fib_max):
    fib_nums = [0,1]
    
    while fib_nums[-1] + fib_nums[-2] <= fib_max:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    
    return print(fib_nums)

def delete_dup(my_list):
    i = 0
    while i < len(my_list):
        j = i + 1
        
        while j < len(my_list):
            if my_list[i] == my_list[j]:
                del my_list[j]
            else:
                j += 1
        i += 1
    return print(my_list)