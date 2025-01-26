a = [1, 3, 5, 6]
b = [5, 6, 7, 8]
c = [7, 8, 9, 10]

res = zip(a, b, c)

# print(set(res))
for val in res:
    print(val, type(val))

l1 = [[1, 2], [3, 4], [5, 6]]
l2 = [[7, 8], [9, 10], [11, 12]]

res = zip(l1, l2)
for val in res:
    print(val, type(val))
    # print('does not print, coz no value, zip return items is an iterator')


def longest_common_prefix(strings):
    prefix = []
    for char in zip(*strings):
        if len(strings) == 1:
            pass


strings = ['Flower', 'Flow', 'Flight']

print(list(zip(*strings)))
