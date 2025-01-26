# 1. Create a function to retrieve back the employee of the month. Consider all edge cases that may come up in the implementation.
# 	I/P: waiter_ids = [1, 2, 3, 3, 2, 1, 3, 1, 2, 3]
# 	     tip_values = [20, 21, 12, 13, 15, 17, 19, 25, 31, 30]
# 	O/P: Waiter ID: 3

# waiter_ids = [1, 2, 3, 3, 2, 1, 3, 1, 2, 3]
# tip_values = [20, 21, 12, 13, 15, 17, 19, 25, 31, 30]
#
# total_tip = dict()
#
# for i in range(len(waiter_ids)):
#     total_tip[waiter_ids[i]] = total_tip.get(waiter_ids[i], 0) + tip_values[i]
#
# max_tip = max_id = 0
# for key, val in total_tip.items():
#     if val>max_tip:
#         max_tip = val
#         max_id = key
#
# print(max_id)


# 2. Given below is a list of dictionaries. Remove the repeating values from the list without using any loops.
# 	I/P: [{'a': 123, 'b': 1234}, {'a': 3222, 'b': 1234}, {'a': 123, 'b': 1234}]
# 	O/P: [{'a': 3222, 'b': 1234}, {'a': 123, 'b': 1234}]

# ip = [{'a': 123, 'b': 1234}, {'a': 3222, 'b': 1234}, {'a': 123, 'b': 1234}]
#
# # print(set(ip))
#
# # op = [item for item in ip if item not in op]
# op = []
# for item in ip:
#     if item not in op:
#         op.append(item)
# print(op)


# Author(id, name), Book(title, author_id, rating)
# Write an SQL query to find top 3 authors based on the average rating of their books
#
# select name
# from author a
# join (
# select author_id, avg(rating) as avg_rating
# from book
# group by author_id
# order by avg_rating desc
# limit 3 ) top
# on a.id = top.author_id;
#
#
# select a.name, avg(rating) as avg_rating
# from author a join book b
# on a.id = b.author_id
# group_by a.name
# order by avg_rating desc
# limit 3


