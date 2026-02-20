"""
Docstring for construct_string_from_binary_tree

Construct String from Binary Tree

Given the root of a binary tree, return a string representation
of the tree using preorder traversal (root → left → right).

Formatting Rules:
- Each node is represented by its integer value.
- If a node has a left child, include it in parentheses: (left_subtree).
- If a node has a right child, include it in parentheses: (right_subtree).
- If a node has only a right child (no left child), include empty
  parentheses "()" before the right subtree to preserve structure.
- If a node has only a left child, omit the right parentheses.
- If a node has no children, return just its value.

The goal is to ensure a one-to-one mapping between the string
representation and the original binary tree.

"""


def solution(root):
    # look if you are given a binary tree, the solution will always be hidden in recursion,
    # yes we might be able to iterate it, but since we are going through more then one branch, then i dont think while loop would work for this

    # so first lets try to right a psudo code
    # "Btw we are doing pre order, so root -> left -> right"
    result = []

    def helper(node):
        if not node:
            return ""

        # now we go through each condition one by one

        # if there are no children
        if not node.right and not node.left:
            return str(node.val)

        # if there is only left child not the right child
        if node.left and not node.right:
            return f"{node.val}({helper(node.left)})"

        # if there is only right child and no left child
        if not node.left and node.right:
            return f"{node.val}()({helper(node.right)})"

        # if nothing then the only condition left is that we have both the children

        # in that case, we return all
        return f"{node.val}({helper(node.left)})({helper(node.right)})"

    return helper(root)
