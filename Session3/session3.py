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
                print(fibonacci_numbers[0:-1])
                break

def duplicate_removal (input_list):
    output_list = []
    for number in range(0,len(input_list)):
        if input_list[number] != input_list[0]:
            if input_list[number] != input_list[(number-1)]:
                output_list.append(input_list[number])
        else:
            output_list.append(input_list[number])
    return output_list