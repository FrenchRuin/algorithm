"""
선택정렬...

제일 작은 것을 가장 앞의 숫자와 교체한다.
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]  # sample

for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j

    array[i], array[min_idx] = array[min_idx], array[i]

print(array)
