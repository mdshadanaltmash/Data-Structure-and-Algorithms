def fib(n):
    assert n>=0 and int(n)==n, 'Fibonnacci numbers cannot be negative numbers or non integer.'
    if n in (0,1):
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(4))


def print_fib_series(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    return print_fib_series(n-1) + print_fib_series(n-2)

n = 7
for i in range(n):
    print(print_fib_series(i), end=" ")



    # 1 1 2 3 5 8 13








