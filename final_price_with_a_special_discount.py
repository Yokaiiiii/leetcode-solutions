"""
You have a list of numbers called prices, where each number represents the cost of an item in a store.
There’s a special deal: if you buy an item, you can get a discount equal to the cost of the next cheaper item that comes after it. If there’s no cheaper item after it, you don’t get a discount.
Your task is to create a new list called answer, where each number shows the final price you’ll pay for each item after applying the discount.

"""

prices = [10, 1, 1, 6]

## Brute force approach

for i in range(len(prices)):
    price = prices[i]
    discount = 0
    for j in range(i + 1, len(prices)):
        if prices[j] <= price:
            discount = prices[j]
            break
    prices[i] = price - discount

print(f"Final Prices = {prices}")
