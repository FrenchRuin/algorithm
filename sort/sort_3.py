"""
계수 정렬

범위가 정해져있을때 가능하다.

각 숫자의 갯수를 설정하여, 그 갯수만큼 출력한다.

"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")
