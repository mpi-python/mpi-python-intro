def fibonacciseries(item):
    numbers = range(1,101)
    fibonacci = [1, 1]
    for i in range(len(numbers) - 1):
        fibonacci.append(fibonacci[i] + fibonacci[i + 1])
    return fibonacci[:item]

    