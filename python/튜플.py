from collections import Counter
def solution(s):
    answer = []
    temp = ''
    num = []
    for i in s:
        if i.isdecimal():
            temp += i
        else:
            if temp:
                num.append(int(temp))
                temp = ''
    for i in Counter(num).most_common():
        answer.append(i[0])
    return answer