"""
Given a rod of length n, the task is to cut the rod in such a way that the total number of segments of length x, y, and z is maximized. The segments can only be of length x, y, and z. 
Note: If no segment can be cut then return 0.

Examples: 

Input: n = 4, x = 2, y = 1, z = 1
Output: 4
Explanation: Total length is 4, and the cut lengths are 2, 1 and 1.  We can make maximum 4 segments each of length 1.


Input: n = 5, x = 5, y = 3, z = 2
Output: 2
Explanation: Here total length is 5, and the cut lengths are 5, 3 and 2. We can make two segments of lengths 3 and 2.


Input: n = 7, x = 8, y = 9, z = 10
Output: 0
Explanation: Here the total length is 7, and the cut lengths are 8, 9, and 10. We cannot cut the segment into lengths that fully utilize the segment, so the output is 0.
"""

"""
4 -> 2, 1, 1
1, 1, 1, 1
1, 1, 2
2, 2
f(4) = f(3) + 1
f(3) = f(2) + 1
f(2) = 1

f(4) = max( f(4-1))

5 -> 5, 3, 2
5
2, 3

# if n not in (x, y, z)
# return 0
if n < x and n < y and n<z
    return 0

if n < min(x, y, z)
    return 0


    
f(4) = f(4-2) + f(4-1) + f(4-1)
f(4) = 1 + max(f(4-2), f(4-1), f(4-1))
f(n) = 1 + max(f(n-x), f(n-y), f(n-z))

5 -> 1+ max(f(5-5), f(5-3), f(5-2))
f(0) -> 0
f(2) -> 1 + max(f(2-5)->0, f(2-3)->0, f(2-2)->0)
f(3) -> 1 + max(f(3-5)->0, f(3-3)->0, f(3-2)->0)
"""

def max_segment(n, x, y, z):
    if n < min(x, y, z):
        return 0
    
    return 1 + max(max_segment(n-x, x, y, z),
                   max_segment(n-y, x, y, z),
                   max_segment(n-z, x, y, z))


def max_segment_memo(n, x, y, z, memo):
    if n == 0:
        return 0
    elif n < 0:
        return -1
    
    if n in memo:
        return memo[n]
    
    cut1 = max_segment_memo(n-x, x, y, z, memo)
    cut2 = max_segment_memo(n-y, x, y, z, memo)
    cut3 = max_segment_memo(n-z, x, y, z, memo)

    curr_max = max(cut1, cut2, cut3)
    
    if curr_max == -1:
        memo[n] = -1
        return -1
    
    memo[n] = 1 + curr_max
    return 0 if memo[n] == -1 else memo[n]

# 7-5 -> 2 -> 2-5
# 7-5 -> 2 -> 2-5
# 7-2 -> 5 -> 5-5, 5-5, 5-2 -> 3 -> 3-5, 3-5, 3-2 -> 
n, x, y, z = 7, 5, 5, 2
memo = {}
print(max_segment(n, x, y, z))
print(max_segment_memo(n, x, y, z, memo))


count = 0
digits1 = {2,4}
digits2 = {3,0}
for d in digits2:
    if d in digits1:
        break
else:
    count += 1
