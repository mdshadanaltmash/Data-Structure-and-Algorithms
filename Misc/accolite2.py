# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")

# a = [i for i in range(1,1001, 2)]
# print(a)
import re

s = "I am preetam"
# r = ('am', '_')
# re.replace(s, r)

# print(s.replace('am', '_'))

r = ''
first = False
prev = ''
for char in s:
    if first:
        if char == 'm':
            r += '_'
        else:
            first = False
            r = r + prev + char
            prev = ''
    else:
        if char == 'a':
            first = True
            prev = char
        else:
            r += char
# print(r)


f = lambda a, b, c: a + b + c

r = f
print(r(2, 4, 5))

a = [1, 2, 3, 4, 5]

# def add(x, y):
#     return x+y

from functools import reduce

add = lambda x: x + 10
odd = lambda x: x % 2 == 1
sum1 = lambda x, y: x + y
res = reduce(sum1, filter(odd, map(add, a)))
print(res)


def uppercase_input(func):
    def wrapper(x):
        return func(x.upper())

    return wrapper


@uppercase_input
def func(x):
    return x


print(func('string'))

input1 = [1, 2, 3, 4, 5]
op1 = [1, 2, 3, 4, 6]

input1 = [1, 2, 3, 4, 9]
op2 = [1, 2, 3, 5, 0]

input3 = [9, 9]
op3 = [1, 0, 0]

# input1 = [str(i) for i in input1]
# str1 = ''.join(input1)
# int1 = int(str1) + 1


# res = str(int1)
# print(res.split())
# print(res)


input1 = input1[::-1]
carry = 0
for i in range(len(input1)):
    if i == 0:
        input1[i] += 1
        if input1[i] > 9:
            input1[i] = input1[i] // 10
            carry = input1[i] % 10
        # if carry>0:
    else:
        if carry > 0:
            # print(input1[i])
            input1[i] = input1[i] + carry

            if input1[i] > 9:
                input1[i] = input1[i] // 10
                carry = input1[i] % 10
            # if carry>0:

print(carry, input1)
if carry > 0:
    n = len(input1) - 1
    input1[n] = input1[n] + carry
    if input1[n] > 9:
        input1[n] = input1[n] // 10
        carry = input1[n] % 10
        input1.append(carry)
print(input1[::-1])

inp = "aaabbccaaa"
op = "a3b2c2a1"

count = 0
curr_char = inp[0]
res = ''
for i in range(len(inp)):
    if inp[i] == curr_char:
        count += 1
    else:
        res += curr_char
        res += str(count)
        count = 1
        curr_char = inp[i]

res += curr_char
res += str(count)

print(res)
