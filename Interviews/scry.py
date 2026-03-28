# [[1,2],[3,4]]
# [1,2,3,4]

def flat_matrix(arr):
    res = []
    for lst in arr:
        res.extend(lst)
    return res


def create_2d_arr(arr, rows, cols):
    # res = [[] * rows]
    lst = []
    # print(res)
    idx = 0
    for i in range(rows):
        lst.append([])
        for j in range(cols):
            lst[i].append(arr[idx])
            idx += 1
    return lst


# a = [[1, 2, 3],
#      [4, 5, 6]]
# rows, cols = len(a), len(a[0])
# flat_arr = flat_matrix(a)
# array_2d = create_2d_arr(flat_arr, rows, cols)
# print(array_2d)


"M(OH)2"
"H2M1O2"
"K4(ON(SO3)2)2"
"K4N2O14S4"
# r = 2, 1
# {H * r, O * 2, M *1}

def mul(char, cnt):
    res = ''
    for s in char:
        res += (s + cnt)


def solution(s):
    l, r, = 0, 1
    res = ''
    while l < r and l < len(s):
        if s[l] == '(':
            while s[r] != ')':
                r += 1
            l += 1
            res += mul(s[l:r-1], r+1)
            r += 3
            l = r
        if s[l].isalpha():
            res += (s[l] + s[r] if s[r].isnumeric() else str(1))
            r += 2
            l = r - 1


print(solution("M(OH)2"))



def atoms(formula: str):
    hash_map = {}
    stack = []

    for char in formula:
        if char.isalpha():
            stack.append(char)
            # if stack == []:
        elif char.isnumeric():
            if stack[-1] == ')':
                stack.pop()
                temp_hash = {}
                while stack[-1] != '(':
                    curr_elem = stack.pop()
                    hash_map[curr_elem] = hash_map.get(curr_elem, 0) + int(char)


# IDP
# collatio , python, cherrypy, stateless, redis, optimze,















