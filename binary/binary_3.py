"""
떡자르기

떡 갯수와 요구한 떡길이를 부여받고
절단기 최대길이를 설정하여 가져간다.

떡 갯수 = 4
요구 떡 길이 = 6
떡 19 15 10 17
"""

N, K = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array) - 1

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in array:
        if i > mid:
            total += i - mid

    if total < K:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
