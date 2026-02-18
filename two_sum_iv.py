# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root, k: int) -> bool:
        flattened_tree = self.flatten_tree(root)
        # now this is truned into a normal two sum problem that we can solve using two pointer
        left = 0
        right = len(flattened_tree) - 1
        while left != right:
            result = flattened_tree[left] + flattened_tree[right]
            if result > k:
                right -= 1
            elif result < k:
                left += 1
            else:
                return True
        return False

    def flatten_tree(self, node):
        # this is gonna do a in order traversal so that so that we get a flattened traversal of the binary search tree
        if not node:
            return []
        else:
            return (
                self.flatten_tree(node.left)
                + [node.val]
                + self.flatten_tree(node.right)
            )
