"""
2269. Find the K-Beauty of a Number

The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:

Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: num = 240, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "24" from "240": 24 is a divisor of 240.
- "40" from "240": 40 is a divisor of 240.
Therefore, the k-beauty is 2.
Example 2:

Input: num = 430043, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "43" from "430043": 43 is a divisor of 430043.
- "30" from "430043": 30 is not a divisor of 430043.
- "00" from "430043": 0 is not a divisor of 430043.
- "04" from "430043": 4 is not a divisor of 430043.
- "43" from "430043": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.


"""



def divisorSubstrings(num: int, k: int) -> int:
    str_num = str(num)
    curr_win = [str_num[i] for i in range(k)]
    k_beauty = 0
    if int(''.join(curr_win)) != 0:
        if num%int(''.join(curr_win)) == 0:
            k_beauty+=1
    for i in range(len(str_num)-k):
        curr_win.pop(0)
        curr_win.append(str_num[i+k])
        if int(''.join(curr_win)) != 0:
            if num%int(''.join(curr_win)) == 0:
                k_beauty+=1
            
    return k_beauty

print(divisorSubstrings(240,2))