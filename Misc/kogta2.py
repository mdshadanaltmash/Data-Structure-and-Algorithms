def decorate(func):
    def wrapper(*args, **kwargs):
        print('before')
        func(*args, **kwargs)
        print('after')

    return wrapper


def decorate1(func):
    def wrapper(*args, **kwargs):
        print('before1')
        func(*args, **kwargs)
        print('after1')

    return wrapper


@decorate1
@decorate
def hello(name):
    print('Hello: ', name)


hello('Shadan')

a = [87, 54, 89, 43, 23, 90, 21, 68, 94, 42, 89, 84, 32]

f = lambda x: x if x % 2 == 0 else False
g = lambda x: x != False
# print(list(map(f, a)))
res = filter(g, map(f, a))


def squares(n):
    for i in range(1, n + 1):
        yield i ** 2


gen_sq = squares(10)

print(next(gen_sq))
print(next(gen_sq))
print(next(gen_sq))
print(next(gen_sq))
print(next(gen_sq))

from copy import copy

a = [1, 2, 4, [10, 30, 50]]
b = copy(a)
b[0] = 11
print(b, a)
b[3][1] = 31
print(b, a)

a = [[1, 2, 3, [19, 14, 25, [78, 54]]], [4, 5], [6, 7], 9, 19, 19, 'a', 'b']


def flat(arr):
    res = []
    for val in arr:
        if isinstance(val, list):
            res.extend(flat(val))
        else:
            res.append(val)
    return res

print(flat(a))


def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


a = [[1, 2, 3, [19, 14, 25, [78, 54]]], [4, 5], [6, 7], 9, 19, 19, 'a', 'b']
flattened = flatten_list(a)
print(flattened)


# 0-4 0 0
# 4-8 5 20
# 8-12 10 40
# 12-16 15 60
# 16-20 20  80
# 20-24 25 100
# 24+ 30