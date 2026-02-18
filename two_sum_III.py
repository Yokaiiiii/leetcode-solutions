"""
Here we are to decide which data structure to design on to to keep the stream of data that is given to use, and then we are supposed to create a function to find if there exists any two numbers that sum up to k
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TwoSum:

    def _init__(self):
        """
        Initialize your data structure here.
        """
        # Think: What structure allows O(1) count checks?
        self.num_counts = {}  # okay we are just using this approach now then

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure.
        """
        self.num_counts[number] = self.num_counts.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        # Logic to iterate and check for (value - num)
        for num in self.num_counts:
            complement = value - num
            if complement in self.num_counts:
                # case 1: were the complement and the num are different values
                if complement != num:
                    return True
                if self.num_counts[num] > 1:
                    return True

        return False
