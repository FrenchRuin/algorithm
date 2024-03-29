"""

이진탐색
반으로 쪼개면서 탐색하기
"""
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


N = int(input())
array = list(map(int, input().split()))
array.sort()

M = int(input())
target = list(map(int, input().split()))

for i in target:
    result = binary_search(array, i, 0, N - 1)
    if result is not None:
        print("YES", end=" ")
    else:
        print("NO", end=" ")
