class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# we are gonna code standalone function to do operation on this tree while jsut taking the root as the argument


# now we are coding a insertaion function to automaticaly insert the value in its correct place
def insert(root, val):
    # this there is no root, then we create a new node with the value and thats our new root
    if not root:
        return TreeNode(val)

    # if the val is les sthen root.val, we move towards left
    if val < root.val:
        # reassign the left pointer to the result of the next call
        root.left = insert(root.left, val)

    else:
        root.right = insert(root.right, val)

    return root


def treeSum(root):
    # this is used to give out the sum of all the values in the tree
    if not root:
        return 0
    else:
        leftsum = treeSum(root.left)
        rightsum = treeSum(root.right)
        return root.val + leftsum + rightsum


def inorder(root):
    if not root:
        return []

    # if we have root then we traverse (in inorder traversal) by left + root + right
    return inorder(root.left) + [root.val] + inorder(root.right)


root = TreeNode(4)
insert(root, 10)
insert(root, 20)
insert(root, 15)
insert(root, 9)
insert(root, 7)
insert(root, 5)
insert(root, 30)


# testing this
print(f"In-Order traversal : {inorder(root)}")
print(f"The sum of the entire binary search tree is : {treeSum(root)}")
