"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    #Solution 1
    for i in range(len(s)//2):
            s[i],s[len(s)-i-1]=s[len(s)-i-1], s[i]

    # #solution 2

    # leng=len(s)
    # if leng%2==0:
    #     for i in range(leng//2):
    #         s[i],s[len(s)-i-1]=s[len(s)-i-1], s[i]
    # else:
    #     for i in range((leng-1)//2):
    #         s[i],s[len(s)-i-1]=s[len(s)-i-1], s[i]

    # #solution 3
    # for i in range(len(s)+1//2):
    #         s.insert(i,s.pop())


arr = ["H","a","n","n","a","h"]
reverseString(arr)
print(arr)