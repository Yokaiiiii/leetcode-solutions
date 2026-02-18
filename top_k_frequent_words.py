"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
"""


def solution(words, k):
    # create hash map
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    sorted_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

    return [sorted_count[i][0] for i in range(k)]


result = solution(
    words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4
)
print(result)
