def solution(info, edges):
    answer = []
    visited = [0] * len(info) 
    visited[0] = 1
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for i in range(len(edges)):
            parent, child = edges[i]
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child] == 1:
                    dfs(sheep, wolf + 1)
                    visited[child] = 0
                elif info[child] == 0:
                    dfs(sheep + 1, wolf)
                    visited[child] = 0
    dfs(1, 0)
    print(answer)
    return max(answer)

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))