"""
Docstring for excel_sheet_column_number

So here we are given an excel column title and we have to return its corresponding number
for example
A -> 1
AA -> 27
ZZ -> 702
AAA -> 703
and so on

so how can we do it?
lets create a dictionary to give each character its numerical value like {A : 1, B : 2, .....}

now we iterate through the title and go from right to left
for each value we do {value * 26 ^ its position} and the sum of all this is our value
"""

columnTitle = "AAA"
reversed_column_title = columnTitle[::-1]
column_numbers = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}

result = 0
position = 0
for item in reversed_column_title:
    result += column_numbers[item] * (26**position)
    print(f" Item = {item}, position = {position}, result = {result}")
    position += 1

print(result)
