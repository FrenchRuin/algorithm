"""

이진탐색
반으로 쪼개면서 탐색하기
"""


def binary_search(array, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

print(binary_search(array, target, 0, n - 1) + 1)
