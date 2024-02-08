"""
떡자르기

떡 갯수와 요구한 떡길이를 부여받고
절단기 최대길이를 설정하여 가져간다.

떡 갯수 = 4
요구 떡 길이 = 6
떡 19 15 10 17

=============|          0
=============|=======   6
=========    |          0
=============|===       3
             |          9
"""

N, M = map(int, input().split())  # 떡 N, 요구 M
array = list(map(int, input().split()))  # 떡 길이들

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            total += i - mid

    if total < M: ## 최소 요구 떡보다 길이가 작으면 범위 설정
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
