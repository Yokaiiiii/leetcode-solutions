"""
Docstring for k_th_smallest_element_in_bst
We are given a binary search tree, we are to give out the k^th smallest number from that bst.

lets look at constraints before thinking of coding
    there are n nodes in the tree
    where
        1 <= k <= n <= 10^4
        meaning that k will always be smaller then or equal to the total number of nodes in the tree and both are gonna be atleast more then 1

    value of node can start from 0 (doesn't add much but whatever)

though process for proceding to code:

    Idea1: we can first perform an inroder traversal, then we can jsut find the (k-1)th value from the flattened list -> lets do this one first
"""


def in_order_traversal(root, res, k):
    if not root or len(res) >= k:
        return

    in_order_traversal(root.left, res, k)
    res.append(root.val)
    in_order_traversal(root.right, res, k)


def flatten_idea(root, k):
    res = []
    in_order_traversal(root, res, k)
    return res[k - 1]
