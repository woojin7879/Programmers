from collections import deque
def solution(places):
    answer = []
    for p in places:
        deq = deque()
        graph = []
        visit = [[False for _ in range(5)]for _ in range(5)]
        for i in p:
            graph.append(list(i))
        num = 0
        for i in range(5):
            for j in range(5):
                if graph[i][j] == 'P':
                    deq.append([i, j, 0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while deq and not num:
            x, y, dis = deq.popleft()
            visit[x][y] = True
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if 0 <= a < 5 and 0 <= b <5 and visit[a][b] == False:
                    if graph[a][b] == 'O' and dis < 2:
                        deq.appendleft([a, b, dis +1])
                    elif graph[a][b] == 'P' and dis < 2:
                        num += 1
        if num:
            answer.append(0)
        else:
            answer.append(1)       
    return answer