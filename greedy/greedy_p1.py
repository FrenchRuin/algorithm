"""

모험가 길드....
공포도로 묶는 그룹을 가져간다.

공포도가 X라면 X명이상으로 구성된 그룹으로 묶여야함

만약에 2 3 1 2 2 라면
3은 3명이상의 그룹에 속해야함

그렇다면 묶일수있는 최대 그룹의 수는?

최소의 공포수부터 묶일수있는 그룹으로 묶는다. = 최대 그룹 갯수
"""
N = int(input())

array = list(map(int, input().split()))

result = 0
count = 0
for i in array:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
