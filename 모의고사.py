def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    right = [0, 0, 0]
    for i in range(len(answers)):
        if first[i%5] == answers[i]:
            right[0] += 1
        if second[i%8] == answers[i]:
            right[1] += 1
        if third[i%10] == answers[i]:
            right[2] += 1
    maxright = max(right)
    for i in range(3):
        if maxright == right[i]:
            answer.append(i+1)
    return answer