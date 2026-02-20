"""
We are given a positive number n, we are to return the number of set (1) bits in n's bits representation.
So example
if n = 11
    ans = 3 since 11 => 1011

So what can we do?
We can conver the number into binary and add the number of 1
now if you ask me how as of now? then no i have no idea how to do it, we learn from this question how to do bit manipulation.

"""


def bit_manipulation(n):
    count = 0
    while n > 0:
        # we check if the 1th position is 1 or not, and we keep on checking it until we convert n -> 0, so by this way we can calculate the number of 1's in the bit representation
        if n & 1:
            count += 1
        n = n >> 1
    return count


print(bit_manipulation(11))
