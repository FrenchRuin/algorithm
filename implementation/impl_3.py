"""
왕실의 나이트

1. 수평으로 두칸 이동한뒤에 수직으로 한 칸 이동하기
2. 수직으로 두칸 이동한뒤에 수평으로 한 칸 이동하기

8x8 크기의 칸이 존재한다.
수직은 1 ~ 8
수평은 a ~ h 로 표현한다.

알파벳을 숫자순서로 가져와야한다.

location = input()
row = location[1]
col = int(ord(location[0])) - int(ord('a')) + 1

print(row, col)
"""
location = input()
row = int(location[1])
col = int(ord(location[0])) - int(ord('a')) + 1

method = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

result = 0
for meth in method:
    new_row = row + meth[0]
    new_col = col + meth[1]
    if 0 < new_row < 9 and 0 < new_col < 9:
        result += 1

print(result)
