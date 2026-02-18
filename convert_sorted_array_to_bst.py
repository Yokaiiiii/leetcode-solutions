"""
We will be given a sorted array [1, 2, 3, 4]. we are to convert it into a height-balanced binary search tree.
Rules to remember:
    1) Sorted array -> numbers are in increasing order.
    2) BST -> leftsubtree < node < rightsubtree
    3) Height bananced -> the heigh of the left and the right subtree can differ by 1 at most.

So what can we do?
(personal though)
we can create a function that takes the sub array, finds its middle element, keeps that as the root and the left of the middle element are inserted into left subtree while the right of the middle element are inserted into right subtree

for this we can create a recursion funciton

how the quesiton is how??
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


array = [1, 2, 3, 4, 5]


def bst_from_array(array, start=0, end=None):
    # so first we check for base case
    if end is None:
        end = len(array)

    if start >= end:
        # meaning the subarray is empty
        return None

    middle_index = (start + end) // 2
    node = TreeNode(array[middle_index])
    node.left = bst_from_array(array=array, start=middle_index, end=end)
    node.right = bst_from_array(array=array, start=start, end=middle_index + 1)
    return node
