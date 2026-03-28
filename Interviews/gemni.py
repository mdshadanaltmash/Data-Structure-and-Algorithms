import time
from functools import reduce

from list import linkedlist

lst = [1, 2, 3, 3, 4, 5, 2, 6, 7, 8, 9, 8]




a = [1, 2, 3, 4, 5]


def is_even(x):
    return x % 2 == 0


def prod(x, y):
    return x * y


print(reduce(prod, filter(is_even, a)))


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(f"Total Time taken is {round((time.time() - start_time),3)}")
        return res
    return wrapper


@timeit
def get_most_freq_elem(arr):
    print("Sleeping for 3 sec")
    time.sleep(3)
    hash_map = {}
    for elem in arr:
        hash_map[elem] = hash_map.get(elem, 0) + 1

    max_count = 0
    res = []
    for key, val in hash_map.items():
        if val > max_count:
            max_count = val
            res = [key]
        elif val == max_count:
            res.append(key)
    return res


print(get_most_freq_elem(lst))


# emp, emp_sal
#
# select emp
# (select emp, rank over(emp_sal desc) as rnk
# from employees
# order by emp_sal desc )
# where rnk = 3;

"""
chat application 

NoSQL


chat (id, group_id, user_id1, user_id2, message)
user
groups(group_id, user_id)
group_dtls(group_id, group_name, created_by, created_at)

"""

"""
pandas join and merge
"""

"""
vpc/subnet
"""


Node(data, next)

for data in list:
    node = Node(data)
    node.next

head

1 -> 2 -> 3 -> 4

prev, next

curr = head

while curr:
    prev = curr
    curr = prev.next
    curr.next = prev

2 -> 1 -> 3 -> 4