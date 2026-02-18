"""
we are given two string s and t
t is made from added a random character to s and shuffling its position.
we need to return the random character.


okay one way to do is, we make a list of frequency of the character for both the strings.
then we find its differnece and the only character with one frequency is the output.


other way to do it.

first we sort both the strings, then we run a loop. if the ith position of both the string are same, we move forward, if not then we say that the character is the random character. LETS TRY THIS FIRST
"""

s = "aecd"
t = "aecbd"

s_sorted = sorted(s)
t_sorted = sorted(t)

for i in range(len(s)):
    if s_sorted[i] != t_sorted[i]:
        print(f"The random character is {t_sorted[i]}")

print(f"the loop is over, the random character is {t_sorted[-1]}")
