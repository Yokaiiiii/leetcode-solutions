def solution1(prices=[7, 1, 5, 3, 6, 4]):
    profit = 0
    for i, buying in enumerate(prices):
        for j, selling in enumerate(prices[i + 1 :]):
            profit = max(profit, selling - buying)
            print(profit)

    return profit


def solution2(prices=[1]):
    profit = 0
    for i, price in enumerate(prices):
        profit = max(profit, price - min(prices[: i + 1]))
        print(profit)
    return profit


def solution3(prices=[7, 1, 5, 3, 6, 4]):
    profit = 0
    minPrice = prices[0]
    for i, price in enumerate(prices):
        minPrice = min(minPrice, price)
        profit = max(profit, price - minPrice)
        print(f"Price = {price}, minPrice = {minPrice}, Profit = {profit}")

    return profit


def harder_solution1(prices=[7, 1, 5, 3, 6, 4, 5]):
    profit = 0
    for i, price in enumerate(prices):
        buy = price
        try:
            sell = prices[i + 1]
        except:
            break
        profit = profit + (sell - buy if sell > buy else 0)
    return profit


ans = harder_solution1()
print(f"the highest profit you can make is {ans}")
