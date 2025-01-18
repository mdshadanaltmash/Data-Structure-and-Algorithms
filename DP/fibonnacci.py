def fib(n, memo):
    # O(n), O(n)
    if n <=1:
        return n
    if memo[n] !=-1:
        return memo[n]
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


def fib_iter(n):
    # O(n), O(n)
    if n<=1:
        return n
    dp = [0] * (n+1)

    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def fib_optimized(n):
    # O(n), O(1)
    if n<=1:
        return n
    prev1, prev2 = 1, 0
    ans = 0
    for i in range(2, n+1):
        ans = prev1 + prev2
        prev2 = prev1
        prev1 = ans
    return ans

n = 7
memo = [-1] * (n + 1)
print(fib(n, memo))
print(fib_iter(n))
print(fib_optimized(n))