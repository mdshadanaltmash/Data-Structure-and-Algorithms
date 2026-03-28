from functools import reduce

numbers = [1, 2, 3, 4, 5]


def square(x):
    return x * x


squared_nums = list(map(square, numbers))
print('lambda func: ', list(map(lambda x: x ** 2, numbers)))
print(squared_nums)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(x):
    return x % 2 == 0


even_nums = list(filter(is_even, numbers))
print('Lambda func: ', list(filter(lambda x: x % 2 == 0, numbers)))
print(even_nums)

numbers = [1, 2, 3, 4, 5]


def add(x, y):
    return x + y


reduced_nums = reduce(add, numbers)
add_func = lambda x, y: x + y
print('Lambda func: ', reduce(add_func, numbers))
print(reduced_nums)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(reduce(lambda x, y: x+y, filter(lambda x: x % 2 == 0, (map(lambda x: x * x, numbers)))))
