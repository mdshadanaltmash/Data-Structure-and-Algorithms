def trib(n, memo):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = trib(n-1, memo) + trib(n-2, memo) + trib(n-3, memo)
    return memo[n]
    

def trib_iter(n):
    # dp (bottom up approach( iterative))

    if n <=1:
        return 0
    elif n == 2:
        return 1
    dp = [-1] * (n+1)
    dp[0], dp[1], dp[2] = 0, 0, 1

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

def trib_optimized(n):
    if n <=1:
        return 0
    elif n == 2:
        return 1
    prev3 = prev2 = 0
    prev1 = 1
    curr = 0

    for i in range(3, n+1):
        curr = prev1 + prev2 + prev3
        prev3 = prev2
        prev2 = prev1
        prev1 = curr
    return curr

n = 10
memo = [-1] * (n+1)
for i in range(n):
    print(trib(i, memo), end=" ")

print()
for i in range(n):
    print(trib_iter(i), end=" ")

print()
for i in range(n):
    print(trib_optimized(i), end=" ")