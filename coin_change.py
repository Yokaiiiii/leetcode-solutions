"""
Docstring for coin_change
oh wow, this is quite challenging

    You are given an integer array coins representing different denominations of coins (coins = [1, 2, 5]) and an integer amount.
    Return the minimum number of coins needed to make up that amount.
    If that amount cannot be made up, return -1.

Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:
    Input: coins = [2], amount = 3
    Output: -1

Example 3:
    Input: coins = [1], amount = 0
    Output: 0


Now lets write the constrints as well:
    1) len(coins) in range [1, 12]
    2) values of count can range from [1, 2^31-1] thats a huge number if you ever aske me
    3) and at last, the value of amount can range from 0 (this has to be noted) till 10^4 (which is also quite a huge number)

Okay we are never told that the coins arry will be in any order, so i am gonna assume that its not ordered properly even though in the examples it ordered properly

okay even though this did came under dynamic programming problem i am not quite sure how to solve it in dynamic programing format

so for now what i have though is,
    we can sort it first
    then start from the highest coin
    add it, if its greater then the amount, move on step further and add it again
    repeat until we either find the amount or we reach the end,

    i believe even if its not the optimal result, this can actually work

    so lets try to code this for now

    AFTER CODING

        the approach we were talking about was greedy approach, but after i figured out that it will not always give out the correct result,
        Why?
            because lets say coins = [1, 3, 4] and the amount = 6, in this case we will return -1 while the actual solution is 2
"""


def solution(coins: list[int], amount: int):
    # base case
    if amount == 0:
        return 0
    coins.sort(reverse=True)  # thsi will sort the coins in descending order

    i = 0
    resulting_amount = 0  # this is the sum of amount after adding each coin
    result = 0  # this is the number of coins needed
    while i < len(coins):
        if resulting_amount + coins[i] > amount:
            i += 1

        elif resulting_amount + coins[i] < amount:
            resulting_amount += coins[i]
            result += 1

        else:
            return result + 1
    return -1
