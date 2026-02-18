"""
we are given a list of string "words"
and we are also given a string "patter"
we need to find how many list word in the words follow the same pattern as in pattern

for example: we are given
    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = "abb"

    here the output will be ["mee", "aqq"]
    since those two follow the same patters

    another example:
    words = ["a","b","c"]
    pattern = "a"
    Output: ["a","b","c"]
    Here we can notice that if the length of "pattern" is 1, then every 1 length word in the words are gonna be the outpu

    so first constraints will be:
        Check the length, only move on to the next step if the length of the word in words is same as length of pattern.



"""


def find_pattern(s, t):
    mapST, mapTS = {}, {}
    for c1, c2 in zip(s, t):
        if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1
    return True


def solution(words, pattern):
    result = []  # this is where we are gonna append all the solutions that match

    length = len(pattern)

    words = [
        word for word in words if len(word) == length
    ]  # this will filter out all the words which doesn't match the length of the pattern

    if (
        length == 1
    ):  # if there is only one character in patter, then every one character match from the words, we dont even need to map anything
        return words

    for word in words:
        if find_pattern(word, pattern):
            result.append(word)

    return result
    # now we can just loop through each of them and call the function that we previously made


response = solution(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb")

print(response)
