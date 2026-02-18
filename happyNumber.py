"""
Docstring for happyNumber

so we are given a number and we gotta find if its a happy number or not
when we are given a number we gotta find the sum of the square of each digit until we get a single digit number
if the single digit number is 1 then its a happy number else, not

how are we gonna do it?
we are just gonna find the sum of square of every digit and replace the origial number with it
add the original number in a list so that we dont repeat the same numbers
if we reach a single digit number then we check if its 1 or not
if the single digit is not 1 and if we repeat any number then we are gonna return False


*okay i presumed it wrong, the condition that the number is not happy is only when that number roates in cicle*

even a single digit number like 7 can be a happy number
"""

visited = []
n = 69

while n != 1:
    visited.append(n)
    result = 0
    while n != 0:
        r = n % 10
        result += r * r
        n = n // 10

    if result in visited:
        break

    n = result
print("happy number")
