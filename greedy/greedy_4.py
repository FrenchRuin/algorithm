"""
왕실의 나이트

8x8의 체스판이있다.

a1 같이 나이트의 위치가 주어진다면 이동할수있는 경우의수를 출력하라

나이트 움직인 방법
    1. 수평으로 2칸움직인후, 수직으로 1칸이동
    2. 수직으로 2칸움직인후, 수평으로 1칸이동


"""

input_data = input()
row = int(input_data[1])  # 1,2,3,4,5,6,7,8,9
col = int(ord(input_data[0].upper()) - ord('A') + 1)  # 알파벳을 숫자로 변경한다.
direction = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, -2), (1, 2), (-1, 2), (-1, -2)]  # 8가지 경우의수
answer = 0
for dir in direction:
    x = row + dir[0]
    y = col + dir[1]
    if 1 <= x <= 8 and 1 <= y <= 8:
        answer += 1

print(answer)
