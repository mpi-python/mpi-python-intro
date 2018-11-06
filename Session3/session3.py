def fibonacci(highest_number):
    to_be_appended = 0
    Fibonacci_sequence = []
    while to_be_appended <= highest_number:
        for number in range(1,101):
            if number == 1:
                Fibonacci_sequence.append(number)
            elif number == 2:
                Fibonacci_sequence.append(1)
            else:
                to_be_appended = Fibonacci_sequence[-1]+Fibonacci_sequence[-2]
                if to_be_appended <= highest_number:
                    Fibonacci_sequence.append(to_be_appended)
    return Fibonacci_sequence 

def delete_duplicates_v1(input_list):
    output_list = []
    for number in input_list:
        if output_list.count(number) == False:
            output_list.append(number)
    return output_list
    
def delete_duplicates_v2(input_list):
    return list(set(input_list))
