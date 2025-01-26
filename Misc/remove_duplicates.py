# Write a Python function to remove duplicate elements from a list while maintaining the order.

a = [1, 3, 4, 2, 1, 5, 6, 4, 7, 7]
seen = set()
res = []
for i in range(len(a)):
    if a[i] not in seen:
        res.append(a[i])
        seen.add(a[i])

print(res)
