"""
You have a string with pairs of brackets, each containing a non-empty key. For example, in “(name)is(age)yearsold”, the keys are “name” and “age”. You have a list of key-value pairs called knowledge, where each pair is like [key, value]. Your job is to go through each bracket pair and:

1. Replace the key inside the brackets with its value from knowledge.
2. If you don’t know the value, replace the key and brackets with a question mark “?”.

Each key will only appear once in knowledge, and there are no nested brackets in the string. Return the string after replacing all the bracket pairs.
"""

s = "(name)is(age)yearsold"
knowledge = [["name", "bob"], ["age", "two"]]


def solution(s: str, knowledge):
    knowledge_dict = {key: value for key, value in knowledge}
    result = []
    key_string = ""
    for char in s:
        if char == "(":
            start = True
            continue
        if char == ")":
            start = False
            # print(f"Key string = {key_string}")
            value = knowledge_dict.get(key_string, "?")
            key_string = ""
            result.append(value)
            continue
        if start:
            key_string += char
        else:
            result.append(char)
    return "".join(result)


result = solution(s, knowledge)

print(result)
