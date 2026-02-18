"""
so we are given a string, and we need to figure out its frequency and return a string with descending order of the frequency.
    ning if the string = "tree", here 'e' is repeated 2 times, and others are just repeated once
    so we output "eetr" or "eert"
"""

"""
So what can we actually do?
Since this problem deals with frequency of the character in the string we can first start off with creating a hash map of character count

after that we can sort the hash map bases on the values of it in descending order

then we can loop through that dictionary and create a new list maybe with key * values, then we can later join then to give out the output string
"""


def solution(s):
    # first we create a hash map
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # now that we have a hash_map with character : frequency

    # now we can sort the dictionary in term of frequency
    char_count = dict(
        sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    )

    # now that we have a dict in descending order of its frequency

    # now we can create a list with character * frequency
    result = [char * freq for char, freq in char_count.items()]
    return "".join(result)


print(solution("Aabb"))
