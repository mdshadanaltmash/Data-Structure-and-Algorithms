"""
You are given a string of 2N characters consisting of N ‘[‘ brackets and N ‘]’ brackets. A string is considered balanced if it can be represented in the form S2[S1] where S1 and S2 are balanced strings. We can make an unbalanced string balanced by swapping adjacent characters. Calculate the minimum number of swaps necessary to make a string balanced.

Examples:

Input  : []][][
Output : 2
First swap: Position 3 and 4
[][]][
Second swap: Position 5 and 6
[][][]

Input  : [[][]]
Output : 0
The string is already balanced.

Link: https://www.geeksforgeeks.org/minimum-swaps-bracket-balancing/

"""

# def minimumNumberOfSwaps(s):
#     # code here
#     stack = []
#     cnt = 0
#
#     for char in s:
#         if (char == '[' or char == ']') and not stack:
#             stack.append(char)
#         elif char == '[' and stack[-1] == ']':
#             cnt += 1
#             stack.pop()
#         elif char == ']' and stack[-1] == '[':
#             stack.pop()
#         elif char == ']' and stack[-1] == ']':
#             stack.append(char)
#         else:
#             stack.append(char)
#     return cnt


# Python3 program to count swaps required to
# balance string
def swapCount(s):
    # Swap stores the number of swaps
    # required imbalance maintains the
    # number of imbalance pair
    swap = 0
    imbalance = 0

    for i in s:
        if i == '[':

            # Decrement the imbalance
            imbalance -= 1
        else:

            # Increment imbalance
            imbalance += 1

            if imbalance > 0:
                swap += imbalance

    return swap


s = '[]][]['
s = '[][][][]]]]][[[['

# print(minimumNumberOfSwaps(s))
print(swapCount(s))
