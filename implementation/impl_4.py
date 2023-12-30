"""

게임개발

세로 N 가로 M
 0 : 북
 1 : 동
 2 : 남
 3 : 서


 0 : 육지
 1 : 바다
"""

N, M = map(int, input().split())
visited = [[0] * M for _ in range(N)]

x, y, direction = map(int, input().split())
visited[x][y] = 1

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break

        turn_time = 0

print(count)


