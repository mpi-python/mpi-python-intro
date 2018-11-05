## 4. Fibonacci function

def fibofun(n):
    a = 0
    b = 1
    fibo = [0, 1]
    for i in range(2, 100):
        x = a + b
        if x < n: 
            fibo.append(x)
            a = b 
            b = x
        else:
            break 
       
    return fibo

## 4. Function to remove duplicates 

import random

def nodups():
    input = [random.randint(1,25) for i in range(25)]
    
    output = list(set(input))
   
    return output