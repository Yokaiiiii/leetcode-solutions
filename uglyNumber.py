"""
Docstring for uglyNumber

we are given a number and if it has factors other then 2, 3, 5 then its not an ugly number. we gotta return if its a ugly number or not.

14 has factor 2, 7 so its not an ugly number
15 has a factor 3, 5 so its a ugly number
Intuition Behind the Code

    Ugly number definition:
        An ugly number is a positive number whose only prime factors are 2, 3, or 5.

    Step 1 – Handle 0:

        If the number n is 0, it cannot be ugly, so we immediately return False.

    Step 2 – Remove all factors of 2, 3, and 5:

        We repeatedly divide n by 2 as long as it’s divisible by 2.

        Then we do the same for 3 and 5.

        This effectively strips away all allowed prime factors from n.

    Step 3 – Check the remainder:

        If after removing all 2s, 3s, and 5s, n becomes 1, it means no other prime factors exist, so the number is ugly → return True.

        If n is greater than 1, it still has some other prime factor(s), so it’s not ugly → return False.

"""

n = 0
step = 1
while n != -1:
    n = int(input("Enter a number "))

    while n % 2 == 0:
        n = n // 2
        print(f" Inside %2: n = {n}, step = {step}")
        step += 1
    while n % 3 == 0:
        n = n // 3
        print(f" Inside %5: n = {n}, step = {step}")
        step += 1
    while n % 5 == 0:
        n = n // 5
        print(f" Inside %5: n = {n}, step = {step}")
        step += 1

    if n <= 1:
        print("ugly number")

    else:
        print("not an ugly number")
