"""

음료수 열려먹기

ex)
3 3
001
010
101

answer = 3
"""

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x - 1, y)
        return True
    return False


answer = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            answer += 1

print(answer)
