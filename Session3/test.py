def fibfunction(fib_number):
    list_fib = [0,1]                                  
    while list_fib[-1] < fib_number:
        list_fib.append(list_fib[-1] + list_fib[-2]) 
    return list_fib[:-1]

def remove_dups(*input):
    return list(set(input))