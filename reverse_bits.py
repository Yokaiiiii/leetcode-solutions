"""
We are given a number and we need to reverse its bits representation.
For example:
    if n = 11
        its bits representation = 1011
        but now if we reverse it we get = 11010000000000000000000000000000

so what we do is, we always consider that the number is 32 bit number
we run a loop 32 times
we take take the lsb of it while rotating the number and append that to a list or something and later join it to get an int value number
"""


def reverse_bits(n):
    result = 0
    for i in range(32):
        lsb = n & 1

        result = (result << 1) | lsb
        # now we update n
        n = n >> 1

    return result
