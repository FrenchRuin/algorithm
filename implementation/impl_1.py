"""

상하좌우

N * N 크기의 지도가 존재한다.
시작위치는 1,1
끝 크기는 N,N이다.
L = 왼쪽으로 한칸 이동
R = 오른쪽으로 한칸이동
U = 위쪽으로 한칸이동
D = 아래쪽으로 한칸이동

"""

N = int(input())  # 지도 크기
x, y = 1, 1  # 시작 위치
command_line = input().split()  # 명령

dx = [0, 0, -1, 1]  # 좌우상하
dy = [-1, 1, 0, 0]  # 좌우상하
move = ['L', 'R', 'U', 'D']

for command in command_line:
    nx, ny = 0, 0
    for i in range(len(move)):
        if command == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

print(x, y)
