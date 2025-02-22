# /*Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.
# Examples
# Example 1:
# Input Format
# : N = 6, array[] = {9, -3, 3, -1, 6, -5}
# max_len=5
# Result
# : 5
# Explanation
# : The following subarrays sum to zero:
# {-3, 3} , {-1, 6, -5}, {-3, 3, -1, 6, -5}
# Since we require the length of the longest subarray, our answer is 5!
# Example 2:
# Input Format:
#  N = 8, array[] = {6, -2, 2, -8, 1, 7, 4, -10}
# Result
# : 8
# Subarrays with sum 0 : {-2, 2}, {-8, 1, 7}, {-2, 2, -8, 1, 7}, {6, -2, 2, -8, 1, 7, 4, -10}
# # Length of longest subarray = 8
# # Example 3:
# # Input Format:
# #  N = 3, array[] = {1, 0, -5}
# # Result
# # : 1
# # Subarray : {0}
# # Length of longest subarray = 1
# # Example 4:
# # Input Format:
# #  N = 5, array[] = {1, 3, -5, 6, -2}
# # Result
# # : 0
# # Subarray: There is no subarray that sums to zero
# # */

# # //{9, -3, 3, 1, 6, 5}

def max_zero_len(arr):
    prefix_map = dict()
    curr_sum = 0
    max_len = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0:
            max_len = i + 1
        if curr_sum in prefix_map:
            max_len = max(max_len, i - prefix_map[curr_sum])
        else:
            prefix_map[curr_sum] = i
    return max_len


lst = [1, 0, -1]
print(max_zero_len(lst))
#
# 1: 0
# 0


# ----------


"""
  Instructions:

  Given a list of student test scores, find the best average grade.
  Each student may have more than one test score in the list.

  Complete the bestAverageGrade function in the editor below.
  It has one parameter, scores, which is an array of student test scores.
  Each element in the array is a two-element array of the form [student name, test score]
  e.g. [ "Bobby", "87" ].
  Test scores may be positive or negative integers.

  If you end up with an average grade that is not an integer, you should
  use a floor function to return the largest integer less than or equal to the average.
  Return 0 for an empty input.

  Example:

  Input:
  [ [ "Bobby", "87" ],
    [ "Charles", "100" ],
    [ "Eric", "64" ],
    [ "Charles", "22" ] ].

  Expected output: 87
  Explanation: The average scores are 87, 61, and 64 for Bobby, Charles, and Eric,
  respectively. 87 is the highest.
"""


def bestAverageGrade(scores):
    """ Returns the best average grade. """
    # TODO: implement this function

    avg_map = dict()

    for score in scores:
        if score[0] in avg_map:
            # avg_map[score[0]] = (avg_map[score[0]] + int(score[1])) / 2
            avg_map[score[0]].append(int(score[1]))
        else:
            avg_map[score[0]] = [int(score[1])]

    curr_avg = max_avg = 0
    for key, val in avg_map.items():
        curr_avg = sum(val) // len(val)
        if curr_avg > max_avg:
            max_avg = curr_avg
    return max_avg


def doTestsPass():
    """ Returns true if the tests pass. Otherwise, returns false """

    # TODO: implement more test cases
    tc1 = [["Bobby", "82"],
           ["Charles", "100"],
           ["Charles", "100"],
           ["Eric", "64"],
           ["Charles", "50"],
           ["Eric", "50"],
           ["Charles", "50"],
           ["Bobby", "50"]]
    return bestAverageGrade(tc1) == 75


if __name__ == "__main__":
    result = doTestsPass()

    if result:
        print("All tests pass\n")
    else:
        print("Tests fail\n")
