"""
성적이 낮은 순서로 학생 출력하기

2
홍길동 95
이순신 77

"""

n = int(input())

array = []

for i in range(n):
    data = input().split()

    array.append((data[0], int(data[1])))

array = sorted(array, key=lambda x: x[1])

for st in array:
    print(st[0], end=" ")
