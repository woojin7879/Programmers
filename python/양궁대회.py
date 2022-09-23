from itertools import combinations_with_replacement
def solution(n, info):
    answer = []
    maxdiff = 0
    for combi in combinations_with_replacement(range(11),n):
        lion = [0] * 11
        diff = 0
        for c in combi:
            lion[c] += 1
        for i in range(11):
            if lion[i] > info[i]:
                diff += (10 - i)
            elif lion[i] <= info[i] and info[i] > 0:
                diff -= (10 - i)
        if diff > 0:
            if diff > maxdiff:
                maxdiff = diff
                answer = []
            if diff == maxdiff:
                answer.append(list(reversed(lion)))
    if len(answer) == 0:
        answer.append([-1])
    answer.sort(reverse = True)
    return list(reversed(answer[0]))
print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))