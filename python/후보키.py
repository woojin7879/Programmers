def solution(relation):
    answer = []
    for i in range(1, 1 << len(relation[0])):
        flag = True
        for a in answer:
            if a & i == a:
                flag = False
                break
        if flag:
            temp = set()
            for j in range(len(relation)):
                temp_str = ""
                for k in range(len(relation[0])):
                    if i & (1 << k):
                        temp_str += str(relation[j][k])
                temp.add(temp_str)
            if len(temp) == len(relation):
                answer.append(i)
                print(i)
                print(temp)
    return len(answer)