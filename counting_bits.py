"""
So the explaination of the question is quite simple
We are given a number 'n', and we are expected to return a list of size n+1
where each position of the list has the number of '1' in its bits representation


Example:
    If n = 2
    ans = [_,_,_]
    for i = 0
        ans[0] = 0 Since there is no '1' in 0ths bit representation
    ans[1] = 1 Since 1's bit represetation = 001, containing one 1
    ans[2] = 1 Since 2's bit representation = 010, containing one 1
    ans[3] = 2 Since 2's bit representation = 011, containing two 1
    ans[4] = 1 Since 2's bit representation = 100, containing one 1
    ans[5] = 2 Since 2's bit representation = 101, containing two 1

Okay so how are we gonna solve this in dynamic programming way

How we can break it down into smaller part
like ans[7] = ans[4] + ans[2] + ans[1]
similalry ans[6] = ans[4] + ans[2]
similarly ans[5] = ans[4] + ans[1]

So what can be the pattern?
If i is a power of 2, then the value is automatically 1
If i is even, then we go ans[i - 2] + ans[2]
if i is odd, then we go ans[i - 1] + ans[1] OKAY THIS PART IS CORRECT, THIS WORKS EVERYTIME
but what about the even number, the even number is not really working
it seems to have a different rule
okay
lets trying to think for even numbers

so for a even number which is not the power of 2
So first find the value for the last value for which power of 2 was valid
for 6 it was 4
for 28 it was 16
similarly for lets say 50 it is 32
and then we break the remining part into again smaller even number
like for 50 = 32 + 18
        18  = 16 + 2

    so we can say for 50 = 32 + 16 + 2
    so it was 3 numbers which are directly under power of 2,
    so we get 3
Okay this pattern seems kinda real so lets try some more with it

lets take a even bigger but random number
lets say ans(72) = ans(64) + ans(8)
         ans(72) = 1 + 1
         ans(72) = 2

okay nice, lets try another number too
lets say ans(132) = ans(128) + ans(4)

okay lets try 100
ans(100) = ans(64) + ans(36)
ans(36) = ans(32) + ans(4)
yes we know both of them
so every time we go for a even number
we just have to find the imidiate smallest power of 2 number and i - that number = the another number
and since we are storing it, already in that same answer array, we can just retrieve it
Damn this logic looks promising
"""


def bit_counting(n):
    # so we are doing is, we can set the base condition then we can run the loop
    if n == 0:
        return [0]  # this is the only base case

    ans = [0] * (n + 1)
    # we start the loop from 3 onwards
    largest_power_of_2 = 2
    for i in range(1, n + 1):
        if i % 2 != 0:
            # this means that i is odd, and for odd, we find its last value (i - 1) and add 1 to it
            ans[i] = ans[i - 1] + 1
        # now for even testing
        # in even we have two condition, either its a value with power of 2 or not
        elif i == largest_power_of_2 * 2:
            #  this means that we found our new largest power of 2, here we just append 1
            ans[i] = 1
            largest_power_of_2 = i
        else:
            # this means that we are dealing with even number and its not the power of 2
            # so we just find the reminder from subtractig i with the largest_power_of_2, find its ans[reminder] and add 1 to it
            reminder = i - largest_power_of_2
            ans[i] = 1 + ans[reminder]

    return ans


print(bit_counting(20))
