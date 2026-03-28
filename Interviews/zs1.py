# --emp
# --    id
# --    salary
# --    name
# --
# --select id, name, salary
# --from (
# --select id, name, salary, rank() over(order by salary desc) rnk
# --from emp)
# --where rnk = 2


def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)


f(2)  # l = [0, 1]
f(3, [3, 2, 1])  #l = [3, 2, 1, 0, 1, 4]
f(3)  #l = [0, 1, 0, 1, 4]
