def fibonaci(max_num):
    fibo = []
    fibo.append(0)
    fibo.append(1)
    counter = 2
    while fibo[counter-1]<max_num: 
        fibo.append(fibo[counter-1]+fibo[counter-2])
        counter +=1  
    print(fibo[1:-1])
 


def unique(num_list):
    return list(set(num_list))


def unique2(num_list):
    new_list = []
    for i in num_list:
       if i not in new_list:
        new_list.append(i)
    return (new_list)

