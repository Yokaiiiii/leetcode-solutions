"""
we are given a binary search tree, and two nodes from that tree, we are to give out the node though which it is split apart.
Pretty simple right?
yes

so what we can do is

if go to the node
check if p and q both are in one side (left or right) of that node, if its in either of the side, we go to that subtree and do it again
but if p and q are split across both the side, then that perticular node is the node that is splitting it apart.

Some of the constraints provided:
    That all the values in the node are unique, no values are repeated. # so we dont have to worry about duplicated
    p and q cannot be equal. this can be kinda important
    p and q are the nodes in that tree, they exist.


Now some of the thigns i noticed form examples are :
    p or q can be the node to split then, if it is then just return itself
        Meaning we can add another base care where node.val == either p or q, return it

Okay now lets code it

"""


def solution(root, p, q):
    # so the first base condition
    # i believe this wont be true ever, but still keeping it, might remove it later
    val = root.val
    max_val = max(p.val, q.val)
    min_val = min(p.val, q.val)

    # lets check if this node is one of p and q or not
    if val in (p.val, q.val):
        return root

    # this will check the condition where if p and q are split acorss by this correct node that return the current node
    elif min_val < val < max_val:
        return root

    elif (p.val < val) and (q.val < val):
        return solution(root.left, p, q)

    else:
        return solution(root.right, p, q)


def iterative_version(root, p, q):
    p_val, q_val = p.val, q.val
    node = root
    while (
        node
    ):  # we run this loop until we return out of it or we reach the end (the later is unlikely)
        # checking if they are on either one side
        # first right side
        val = node.val
        if (p_val > val) and (q_val > val):  # meaning both are on the right side
            node = node.right

        elif (p_val < val) and (q_val < val):  # meaning both are on the left side
            node = node.left

        else:
            return node
