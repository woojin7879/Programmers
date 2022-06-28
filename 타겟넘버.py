def solution(numbers, target):
    answer = 0
    def dfs (numsum, i):
        nonlocal answer
        if i == len(numbers):
            if numsum == target:
                answer += 1
            return
        else:
            dfs(numsum - numbers[i], i + 1)
            dfs(numsum + numbers[i], i + 1)
    dfs(-numbers[0], 1)
    dfs(numbers[0], 1)
    return answer