from collections import Counter
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    first = []
    second = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            first.append(str1[i] + str1[i + 1])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            second.append(str2[i] + str2[i + 1])
    c1 = Counter(first)
    c2 = Counter(second)
    intersection = sum((c1&c2).values())
    union = sum((c1|c2).values())
    if not union and not intersection:
        answer = 1
    else:
        answer = intersection / union
    return int(answer * 65536)