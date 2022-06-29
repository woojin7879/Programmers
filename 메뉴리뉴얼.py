from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        combi = []
        for o in orders:
            for i in combinations(o, c):
                arranged = "".join(sorted(i))
                combi.append(arranged)
        sortcombi = Counter(combi).most_common()
        for s in sortcombi:
            if s[1] > 1 and s[1] == sortcombi[0][1]:
                answer.append(s[0]) 
    return sorted(answer)