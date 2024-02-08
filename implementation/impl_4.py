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

N, M = map(int, input().split())  # NxM 맵 4,3

visited = [[0] * M for _ in range(N)]  # 방문한곳
x, y, direction = map(int, input().split())  # 현재 위치 x,y 와 바라보고있는 방향 direction
visited[x][y] = 1  # 서있는곳은 방문처리

arr = []
for i in range(N):  # 지도 입력
    arr.append(list(map(int, input().split())))

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def turn_left():  # 좌로 방향회전
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시작
count = 1
turn_time = 0
while True:
    turn_left()  # 좌로회전
    nx = x + dx[direction]
    ny = y + dy[direction]
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:  # 방문하지 않았거나 지도상 육지라면
        x = nx
        y = ny
        count += 1  # 횟수증가
        turn_time = 0  # 회전횟수 초기화
        continue
    else:
        turn_time += 1

    if turn_time == 4:  # 4번 다 회전한 경우라면?
        nx = x - dx[direction]
        ny = y - dy[direction]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break

        turn_time = 0

print(count)
