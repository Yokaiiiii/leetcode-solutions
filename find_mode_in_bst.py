"""
Docstring for find_mode_in_bst
So we are given a binary search tree with duplicates, meaning there can be more then one occerance of a number in the tree.
We are to give out the number which has repeated the most number of time
i say its easy enough

lets see the constraints:
    There will be atleast 1 node and at most 10^4 nodes.
        So we should kinda think about time complexity

    Values can range from -10^5 to 10^5, thats a hude range but whatever

anyways the thinking process

Idea 1:
    What we can do is since this problem deals with the frequency of the item, we can create frequency dictionary (hash map) while iterating through the tree

    Then sort it based on the frequency (which  we can i guess optimize cause we only need one value not all of them)

    Then give out the first value in the sorted dictionary

    (I hope it makes sense)
"""


def solution(root):
    hash_map = {}

    def iterate(node, hash_map):
        if not node:
            return None

        iterate(node.left, hash_map)
        hash_map[node.val] = hash_map.get(node.val, 0) + 1
        iterate(node.right, hash_map)

    iterate(root, hash_map)
    # now we have a hash_map with key = node.val and values = frequency

    # now we sort it based on frequency
    sorted_list = sorted(hash_map.items(), key=lambda item: -item[1])
    max_frequency = sorted_list[0][1]
    return [key for key, value in hash_map.items() if value == max_frequency]


"""Might not be the best, but it is what it is"""
