"""
숫자 카드 게임

N x M 의 형태의 카드가 존재한다.

특정행에서 최소의 수들을 골라 그중에서 최대의 값을 찾아내야한다.

"""

"""
min을 활용한 방법 

n, m = map(int, input().split())

result = 0

for i in range(n):
    line = list(map(int, input().split()))
    min_value = min(line)
    result = max(min_value, result)

print(result)
"""

"""
# 2중 FOR 문
n, m = map(int, input().split())

result = 0

for i in range(n):
    line = list(map(int, input().split()))
    min_value = 10001
    for j in line:
        min_value = min(min_value, j)

    result = max(result, min_value)

print(result)
"""
