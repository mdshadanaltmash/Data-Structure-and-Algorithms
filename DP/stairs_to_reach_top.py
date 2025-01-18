"""
There are n stairs, and a person standing at the bottom wants to climb stairs to reach the top. The person can climb either 1 stair or 2 stairs at a time, the task is to count the number of ways that a person can reach at the top.

Input: n = 1                                                                                                                                                 
Output: 1 
Explanation: There is only one way to climb 1 stair.                                                                                          

Input: n = 2
Output: 2 
Explanation: There are two ways to reach 2th stair: {1, 1} and {2}.  

Input: n = 4 
Output: 5 
Explanation: There are five ways to reach 4th stair: {1, 1, 1, 1}, {1, 1, 2}, {2, 1, 1}, {1, 2, 1} and {2, 2}. 

"""

"""
n = 1
return 1
n = 2 
return 2

n == 3
return f(n-1) + f(n-2) -> 3
n == 4
return f(n-1) + f(n-2) -> 5

1, 1, 1, 1
1, 1, 2
1, 2, 1
2, 1, 1
2, 2

"""

def solution(n):
    if n <= 2:
        return n
    
    return solution(n-1) + solution(n-2)


def solution_dp_memo(n, memo):
    if n <=2:
        return n
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = solution_dp_memo(n-1, memo) + solution_dp_memo(n-2, memo)
    return memo[n]

def solution_dp_iter(n):
    if n <=2:
        return n
    
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 2
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n-1]


n = 5
memo = [-1] * (n+1)
print(solution(n))
print(solution_dp_memo(n, memo))
print(solution_dp_iter(n))
