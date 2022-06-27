def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        temp = s[0:i]
        length = len(s)
        same = 1
        for j in range(i, len(s), i):
            if s[j:j + i] == temp:
                length -= i
                same += 1
            else:
                if same > 1:
                    length += len(str(same))
                temp = s[j:j + i]
                same = 1
        if same > 1:
            length += len(str(same))
        answer = min(length, answer) 
    return answer