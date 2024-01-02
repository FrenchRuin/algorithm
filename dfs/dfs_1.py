"""
음료수 얼려먹기

구멍이 뚫려있는 부분은 0
칸막이가 존재하는부분은 1

예를들어 4x5 크기의 틀이있다고 가정해보자.

0 0 1 1 0
0 0 0 1 1
1 1 1 1 1
0 0 0 0 0

여기서 0의 영역만 생각한다면 3개의 아이스크림을 만들수있다.

DFS를 사용하여 가능하다. 상하좌우 모두 돈다.
"""

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x, y - 1)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
