from collections import deque
def solution(s):
    answer = 0
    if len(s) % 2 == 1:
        return 0
    a = deque(s[0])
    b = deque(s[1::])
    while b:
        p = b.popleft()
        if len(a) == 0:
            a.append(p)
        elif p == a[-1]:
            a.pop()
        else:
            a.append(p)
    if len(a) == 0:
        return 1
    return 0