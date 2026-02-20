"""
Docstring for climbing_stairs_dp
You are climbing a staircase. It takes n steps to reach the top.
You can either take 1 step or 2 stept to climb the stairs, so you are to return how many distinct ways can you climb to the top?

# so we are using dynamic programming for this
i am just learning about it while solving this problem

So we have two different approach to solve this using dynamic programming
1) Bottom  up approach where we start by the smallest problem and move up
    this is typically done using iteration
2) Top down approach, where we start from the biggest problem and solve it down to the base case to find the solution
    This is usually done using recursion and storing the values from lower level to help the upper lavels
"""


def climbing_stairs(n):
    def top_down_approach(n):
        # Here we are implementing the top down approach to solve this problem
        memo = {}

        def dfs(k: int) -> int:
            # base cases
            if k == 1:
                return 1
            if k == 2:
                return 2
            if k in memo:
                return memo[k]

            # if its not in memo and not a base case then compute it using recursion
            memo[k] = dfs(k - 1) + dfs(k - 2)
            return memo[k]

        return dfs(n)

    def bottom_up_approach(n):
        # here we are implementing the bottom up approach where we start by the smallest case and build up to the bigger problem
        # base case
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev1 = 2  # this is dfs(k-1)
        prev2 = 1  # this is dfs(k-2)
        for i in range(3, n + 1):
            result = prev1 + prev2
            prev1, prev2 = result, prev1

        return result
