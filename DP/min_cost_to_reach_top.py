"""
Given an array of integers cost[] of length n, where cost[i] is the cost of the ith step on a staircase. Once the cost is paid, we can either climb one or two steps.
We can either start from the step with index 0, or the step with index 1. The task is to find the minimum cost to reach the top of the floor.

Examples: 

Input: cost[] = [10, 15, 20]
Output: 15
Explanation: The cheapest option is to start at cost[1], pay that cost, and go to the top.


Input: cost[] = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6 
Explanation: The cheapest option is to start on cost[0], and only step on 1s, skipping cost[3].
"""

"""
if n == 1
return 0
if n == 2
return 1
if n == 3
return min(f(2)*cost[2], f(1)*cost[1])

cost(n) = min(f(n-1)*cost[n-1], f(n-2)*cost[n-2])
 
"""

def min_cost(n, cost):
    if n <=1:
        return cost[n]
    
    return cost[n] + min(min_cost(n-1, cost), min_cost(n-2, cost))

def min_cost_driver(cost):
    # if n <=1:
    #     return
    n = len(cost)
    if n == 1:
        return cost[0]
    return min(min_cost(n-1, cost), min_cost(n-2, cost))


def min_cost_memo(n, cost, memo):
    if n <= 1:
        return cost[n]
    if memo[n] != -1:
        return memo[n]
    memo[n] = cost[n] + min(min_cost_memo(n-1, cost, memo),
                            min_cost_memo(n-2, cost, memo))
    return memo[n]

def min_cost_driver_memo(cost):
    n = len(cost)
    memo = [-1] * (n)
    if n==1:
        return cost[0]
    return min(min_cost_memo(n-1, cost, memo), min_cost_memo(n-2, cost, memo))





cost = [16, 19, 10, 12, 18]
print(min_cost_driver(cost))
print(min_cost_driver_memo(cost))
