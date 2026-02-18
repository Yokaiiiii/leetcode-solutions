"""
We will be given two inputs
one is gonna be pattern while the other is gonna be a string s

we gotta find if s follows the same pattern or not.

so in patter we are given some letters and in string s we are given some words
we need to map exactly one letter in patter exactly one unique word in s
at the same time we need to map unique word in s to exactly one letter in pattern

example:
    pattern = "abba"
    s = "dog cat cat dog"
    here a -> dog, dog -> a
    also b -> cat, cat -> b

another example:
    patter = "abba"
    s = "dog cat cat fish"
    here a -> dog, dog -> a
    also b -> cat, cat -> b
    but since a already mapped to dog, it cannot map to fish again
    and fish cannot map to a because dog has already mapped to a

Given constraints:
    so its not given that len of character in patter == len of words in s
        TODO: so we gotta check this too
"""


def word_patter(pattern, s):
    s = s.split(" ")  # now s is a list of words, now we can finally map them together

    # check if length of character == length of words
    if len(pattern) != len(s):
        return False
    mapCW, mapWC = {}, {}
    for c, w in zip(pattern, s):
        if (c in mapCW and mapCW[c] != w) or (w in mapWC and mapWC[w] != c):
            return False
        mapCW[c] = w
        mapWC[w] = c

    return True


response = word_patter(pattern="abbc", s="dog cat cat dog")
print(response)
