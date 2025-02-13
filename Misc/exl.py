a = [23, 4, 29, 67, 43, 64]

f_max = s_max = 0
for num in a:
    if num >= f_max:
        s_max = f_max
        f_max = num
    elif num > s_max and num<=f_max:
        s_max = num

print(s_max)

a.sort()
print(a[-2])


# nums = [3,4,5,6], target = 7
# Output: [0,1]

nums = [3,4,5,6]
target = 9
mp = dict()
for i, val in enumerate(nums):
    if target-val in mp:
        print(mp[target-val], i)
    mp[val] = i


# (emp_id, name, salary, dept_id)
# (101, 'sohan', '3000', '11'),
# (102, 'rohan', '4000', '12'),
# (103, 'mohan', '5000', '13'),
# (104, 'cat', '3000', '11'),
# (105, 'suresh', '4000', '12'),
# (109, 'mahesh', '7000', '12'),
# (108, 'kamal', '8000', '11');



# select name, salary
# (
# select name, salary, dense_rank() over(partion by dept_id order by salary asc) as rnk
# from table)
# where rnk == 2;

