## LeetCode 921. Minimum Add to Make Parentheses Valid

'''
Given a string s of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
'''
def minAddToMakeValid( s: str) -> int:
    stack=[]
    for i in s:
        if stack==[]:
            stack.append(i)
        elif stack[-1]=='(' and i==')':
            stack.pop()
        else:
            stack.append(i)
    return len(stack)

print(minAddToMakeValid("()))(("))