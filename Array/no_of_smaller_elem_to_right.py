import bisect


def no_of_smaller_elements_to_right(arr):
    res = []
    for i in range(len(arr)):
        cnt = 0
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                cnt += 1
        res.append(cnt)
    return res


def no_of_smaller_elements_to_right_optimized(arr):
    result = []
    seen = []
    for num in reversed(arr):
        i = bisect.bisect_left(seen, num)
        result.append(i)
        bisect.insort(seen, num)
    return list(reversed(result))


if __name__ == '__main__':
    lst = [3, 4, 9, 6, 1]
    print(no_of_smaller_elements_to_right(lst))
    print(no_of_smaller_elements_to_right_optimized(lst))
