def fibonacci(maxFN):
    if maxFN == 0:
        return([0])
    
    fibNumbers = []

    for i in range(0,maxFN+3):
        if i < 2:
            if i <= maxFN:
                fibNumbers.append(i)
        else:
            fN = fibNumbers[i-1]+fibNumbers[i-2]
            if fN <= maxFN:
                fibNumbers.append(fN)
            else:
                return(fibNumbers)
                break

def uniquefier(input_list):
    output_list = []
    for i in range(0,len(input_list)):
        if input_list[i] not in output_list:
            output_list.append(input_list[i])

    return(output_list)