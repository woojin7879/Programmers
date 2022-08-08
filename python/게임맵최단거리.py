from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = n * m + 1
    visit = [[False] * m for _ in range(n)]
    visit[0][0] = True
    deq = deque()
    deq.append([0,0,1])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while deq:
        x, y, l = deq.popleft()
        visit[x][y] = True
        if x == n - 1 and y == m - 1:
            answer = min(answer, l)
            break
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m:
                if visit[a][b] == False and maps[a][b] == 1:
                    visit[a][b] = True
                    deq.append([a, b, l + 1])
    if answer == n * m + 1:
        return -1
    return answer