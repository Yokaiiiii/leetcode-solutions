class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)  # this will be the size of the sliding window
        n2 = len(
            s2
        )  # this will help us know when we are done checking all the values in the string s2

        # now lets create a count of character in each string
        count1 = [0] * 26  # since there are 26 possible alphabets
        count2 = [0] * 26  # same

        # this is just a small check that checks that if s1 is smaller then s2 then there is no way that s2 will contain s1's permutation
        if n1 > n2:
            return False

        # now loading the counts
        for i in range(n1):
            count1[
                ord(s1[i]) - ord("a")
            ] += 1  # this will find the characters's coresponding place in the list and add 1 to indicate its frequency
            # we can do that for the first window in s2 as well here itself
            count2[ord(s2[i]) - ord("a")] += 1

        if count1 == count2:
            return True

        for i in range(n1, n2):
            # for adding new character to the window
            count2[ord(s2[i]) - ord("a")] += 1

            # now for removing
            count2[ord(s2[i - n1]) - ord("a")] -= 1

            # checking
            if count1 == count2:
                return True

        return False
