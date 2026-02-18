"""
Docstring for validate_bst
So this problem is related with validating if the given binary tree is binary search tree or not
    bst means that every value will go to the left of the root node if its less then it, but if it is greater then the root node then it goes to the right of it
In short:
    The left subtree contains values strickly less then the root node
    The right subtree contains values strickly greater then the root node

    And both the left and the right subtree should also be binary search tree

Okay lets think of ways how we can solve it
Idea 1:
    We know what if we traverse the bst in in-order traversal then we get a ascending order list -> time complexity = O(n)
    Then we check if the ascending order is valid or not -> time complexity = O(n)

    So in total this solution will result in O(n) time complexity

Idea 2:
    Wait on a second though, we dont need to figure out the complete flatten list
    we can just add a new clause in the in-order traversal code to check if the node.left.val < node.val or not and similary to the node.right.val > node.val or not
    and we can do this recursively.
    In this way we dont have to create a new list nor do we have to itterate though that list again later on

Idea 3:
    We can deduce the highest value of the left subtree and compare it with the node,
        If the node's value is greater then the highest value in the left subtree then its valid
    Similarly
        If the node's vlaue is less then the lowest value in the right subtree then its valid again

    # lets try to implement this
        On second though, i feel like this way we can only find the higest or the lowest value in the entire subtree, but not what we are hoping to right now
"""


def solution(root):
    def validate(node, low, high):
        if not node:
            return True  # empty subtree is valid

        # check the current node against the high bound
        if not (low < node.val < high):
            return False

        # recurse on left and right with updated bounds
        return validate(node.left, low, node.val) and validate(
            node.right, node.val, high
        )

    # start with infinite bounds at the root

    return validate(root, float("-inf"), float("-inf"))
