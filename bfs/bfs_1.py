"""
미로탈출 복습  >>

NxM 크기의 맵이 존재

N,M까지의 도달할수있는 최단거리 추출

0,0 에서 시작 한다.
즉, N-1,M-1 의 값을 구하면 된다.
하나씩 갈때마다 하나씩 증가하여 처리한다.
"""
# deque를 활용하여 queue 구현 BFS 브루트포스 이기 떄문에
# DFS의 경우에는 Stack을 주로 활용한다 [재귀]
from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N - 1][M - 1]


print(bfs(0,0))
