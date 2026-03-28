# Q. Explain your project
# Q. what is master data management?
# Q. you have joined Capgemini recently so why are you switching again
# Q. What is the difference between Database and Data warehouse?
# Q. When would you use Database and Data warehouse?
# Q. What are SCDs?
# Q. what is star and snowflake schema?
# Q. SQL questions
# Q. explain the order of execution of sql query.
# Q. SQL questions on YOY change of product sells
# Q. Python questions

s = '([{)'
s = '([{}])'

mapping_dict = {')': '(', '}': '{', ']': '['}
stack = []
for char in s:
    # if stack and stack[-1]
    if char in mapping_dict:
        if stack and mapping_dict[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    else:
        stack.append(char)

print(stack == [])


#     if char == ')':
#         if stack and stack[-1] == '(':
#             stack.pop()
#         else:
#             stack.append(char)
#
#
# ['(', '[', '{', ')']


arr = [0, 1, 0, 0, 0, 0, 1, 1]

l, r = 0, len(arr) - 1
while l < r:
    if arr[l] == 0:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    else:
        l += 1
print(arr)


while l < r:
    if arr[r] == 0:
        r -= 1
        continue
    if arr[l] == 0:
        arr[l], arr[r] = arr[r], arr[l]
        r -= 1
    l += 1




















