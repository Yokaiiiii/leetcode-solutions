"""
we are given two string s and t
if the characters in the s REPLACED to get t, then s and t are isomorphic
the order of the character should be preserved
one character can only be replace by another character for the whole word


eg: s = "egg"
    t = "add"

    since 'e' -> 'a'
    and   'g' -> 'd'

so s and t are isomorphic

So some of the constraints, end cases
        1) If the length of the two numbers are not same then they cannot be isomorphic.
        2) Might be brute force but
                1) we take two pointer and slide it through s and t
                2) we create a dict to track the character to be replace and be replaced with
                3) Then we slide the pointer, first check in s, see what should that character be replaced according to the dict
                4) if no record, then replace it by the character from t, and update the dict
                5) At the end of it, check if two string are same or not

Time constraint of Brute force
1(length check) + N(sliding two pointer) + 1(updating the library)
so at max it will be N^2 cause we are also itterating the dict items to see the previous record
"""


def isomorphic_string(s: str, t: str):
    mapST, mapTS = {}, {}
    for c1, c2 in zip(s, t):
        if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1
    return True


response = isomorphic_string("papar", "title")
print(response)
