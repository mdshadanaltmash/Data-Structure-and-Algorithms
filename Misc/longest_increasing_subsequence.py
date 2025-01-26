# How would you find the longest increasing subsequence in a list of integers?

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(n):
        print(i)
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    print(dp)
    return max(dp)


arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(arr))