"""

We are given a string "s" and we are to return the index of the first character which is not repeating in the string.
if all the character are repeating then return -1

"""

"""
So how can we solve this?

we can loop through all of the item and check it, but its gonna take too long O(N^2) -> not ideal

so what we can do instead is, we can create a hash map of every time with their repeatition
if there is no value = 1, then we return -1
We love through the string again and
The first character you encounter that has a count of 1 in your hash map is your answer.
"""


def solution(s):
    # we are given that the length of this string s can be 1 as well, so we check it and return 0 if thats the case
    if len(s) == 1:
        return 0
    # we first create the hash map
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    # this will give us the hash map associated with every character and their count

    # now we check if we have 1 in the values or not, if not then we directly return -1
    if 1 not in char_count.values():
        return -1

    # now we are sure that there is more then one character in the string and there is atleast one character that is not reapeating in the string
    # now we loop through the string one more time and return the index of the first character that has value of 1 in hash_map
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i


print(solution("loveleetcode"))
