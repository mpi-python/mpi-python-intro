def fib_list(fib_max):
    fib_nums = [0,1]
    
    while fib_nums[-1] + fib_nums[-2] <= fib_max:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    
    return print(fib_nums)