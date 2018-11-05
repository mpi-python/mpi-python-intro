def fibonacci(highest):
    fibonacci = [1,1]
   
    for number in range(98):
        if fibonacci[-1] + fibonacci[number] < highest:
            fibonacci.append(fibonacci[number] + fibonacci[number+1])
        else:
            break
        
    return fibonacci

def no_duplicates(input_list):

    output_list = []
    
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
             
    return output_list       
