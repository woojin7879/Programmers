def solution(progresses, speeds):
    answer = []
    n = 0
    while True:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        num = 0
        for i in progresses[n::]:
            if i >= 100:
                num += 1
            else:
                break
        if num:
            answer.append(num)
            n += num
            if n == len(progresses):
                break
    return answer