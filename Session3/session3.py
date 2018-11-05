def fibonacci(highest_num):
    fibonacci_list = [0,1]
    while fibonacci_list[-1] <= highest_num:
        fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
    return fibonacci_list[:-1]

def minus_duplicates (*input_list):
    return list(set(input_list))

def minus_duplicates_loop(*input_list2):
    output_list2 = []
    values = set()
    for item in input_list2:
        if not item in values:
            output_list2.append(item)
            values.add(item)
    return output_list2