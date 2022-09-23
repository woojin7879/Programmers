def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic = {}
    dic1 = {}
    sreport = set(report)
    for i in id_list:
        dic[i] = []
        dic1[i] = 0
    for r in sreport:
        a, b = r.split()
        dic[a].append(b)
        dic1[b] += 1
    for key, val in dic1.items():
        if val >= k:
            for j in range(len(id_list)):
                if key in dic[id_list[j]]:
                    answer[j] += 1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))