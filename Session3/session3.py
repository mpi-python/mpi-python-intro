def fibonacci(highest_num):
    fib_list = [0,1]
    while fib_list[-1] < highest_num:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

def remove_duplicates(input_list):
    output_list = []
    for n in input_list:
        if output_list.count(n) < 1:
            output_list.append(n)
    return output_list