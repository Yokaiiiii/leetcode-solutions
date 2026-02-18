def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    lst = [dic[i] for i in s]
    print(lst)

    i = 0
    j = 1
    sum = lst[i]
    while j < len(lst):
        if lst[i] >= lst[j]:
            sum += lst[j]
        else:
            sum = (sum - lst[i]) + (lst[j] - lst[i])
        i += 1
        j += 1
    return sum


result = romanToInt("III")

print(result)
