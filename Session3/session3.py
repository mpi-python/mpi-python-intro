<<<<<<< HEAD
def fibonacci (max_num):
    numbers = list(range(101))
    fibonacci_seeds = [0,1]
    fibonacci_numbers = [0]
    for number in numbers:
        if number == numbers[1]:
            fibonacci_numbers.append(number)
        elif number >= numbers[1]:
            fibonacci_numbers.append(fibonacci_numbers[number-1] + fibonacci_numbers[number-2])
            if fibonacci_numbers[-1] > max_num:
                return fibonacci_numbers[0:-1]
                break

def duplicate_removal (input_list):
    output_list = []
    for number in range(0,len(input_list)):
        if input_list[number] != input_list[0]:
            if input_list[number] != input_list[(number-1)]:
                output_list.append(input_list[number])
        else:
            output_list.append(input_list[number])
=======
def fibonacci (max_num):
    numbers = list(range(101))
    fibonacci_seeds = [0,1]
    fibonacci_numbers = [0]
    for number in numbers:
        if number == numbers[1]:
            fibonacci_numbers.append(number)
        elif number >= numbers[1]:
            fibonacci_numbers.append(fibonacci_numbers[number-1] + fibonacci_numbers[number-2])
            if fibonacci_numbers[-1] > max_num:
                return fibonacci_numbers[0:-1]
                break

def duplicate_removal (input_list):
    output_list = []
    for number in range(0,len(input_list)):
        if input_list[number] != input_list[0]:
            if input_list[number] != input_list[(number-1)]:
                output_list.append(input_list[number])
        else:
            output_list.append(input_list[number])
>>>>>>> 8cb6f900086be036d6db81373fc67d56b8e9b859
    return output_list