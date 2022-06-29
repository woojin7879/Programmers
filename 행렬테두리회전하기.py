def solution(rows, columns, queries):
    answer = []
    graph = [[(columns * i + j + 1) for j in range(columns)]for i in range(rows)]
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        x2 -= 1
        y1 -= 1
        y2 -= 1
        temp = graph[x1][y1]
        least = graph[x1][y1]
        for i in range(x1, x2):
            n = graph[i+1][y1]
            graph[i][y1] = n
            least = min(least, n)
        for i in range(y1, y2):
            n = graph[x2][i+1]
            graph[x2][i] = n
            least = min(least, n)
        for i in range(x2, x1, -1):
            n = graph[i-1][y2]
            graph[i][y2] = n
            least = min(least, n)
        for i in range(y2, y1, -1):
            n = graph[x1][i-1]
            graph[x1][i] = n
            least = min(least, n)
        graph[x1][y1 + 1] = temp
        answer.append(least)
    return answer