def max_sub_array_sum(arr):
    max_sum = float("-inf")
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            max_sum = max(curr_sum, max_sum)
    return max_sum


def max_sub_array_sum_kadane(arr):
    curr_max_sum = 0
    max_res_sum = 0
    for num in arr:
        curr_max_sum = max(num, curr_max_sum+num)
        max_res_sum = max(curr_max_sum, max_res_sum)
    return max_res_sum


if __name__ == '__main__':
    lst = [34, -50, 42, 14, -5, 86]
    print(max_sub_array_sum(lst))
    print(max_sub_array_sum_kadane(lst))
