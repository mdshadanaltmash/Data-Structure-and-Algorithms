def min_subarray_sum(arr):
    min_res = float("inf")
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            min_res = min(min_res, curr_sum)
    return min_res


def min_subarray_sum_kadane(arr):
    curr_min = min_res = float("inf")

    for num in arr:
        curr_min = min(num, curr_min+num)
        min_res = min(min_res, curr_min)
    return min_res


if __name__ == '__main__':
    lst = [34, -50, 42, 14, -5, 86]
    print(min_subarray_sum(lst))
    print(min_subarray_sum_kadane(lst))
