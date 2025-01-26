arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
# return all the unique pair such that i!=j, and arr[i] + arr[j] = 0

target = dict()
res = []
res_basic = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == 0:
            res_basic.append((arr[i], arr[j]))

for i in range(len(arr)):
    curr_target = 0-arr[i]
    if target.get(curr_target) is not None:
        res.append((i, target[0 - arr[i]]))
    else:
        target[arr[i]] = i

print(res)
print(res_basic)

target_set = set()
res_set = []


for i in range(len(arr)):
    curr_target = 0-arr[i]
    if curr_target in target_set:
        res_set.append((arr[i], 0 - arr[i]))
    else:
        target_set.add(arr[i])

print(res_set)