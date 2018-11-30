fib = [0, 1]
for i in range(100):
    fib.append(fib[i] + fib[i + 1])
    
fibo = []
def fibonacci(n):
    for i in fib:
        if i < n:
            fibo.append(i)
        else:
            break
    return fibo


def delete_dup(n):
    return list(set(n))


def delete_duplicates(n):
    new_list = []
    for i in n:
        if i not in new_list:
            new_list.append(i)
    return new_list


