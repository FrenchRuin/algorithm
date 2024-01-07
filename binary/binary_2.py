"""
부품찾기

N = 5
[8,3,7,9,2]

M = 3
[5,7,9]

N은 가지고있는것
M은 요청한것
요청한게 있으면 yes
없으면 No를 print

"""

N = int(input())
array = set(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

for i in target:
    if i in array:
        print("yes", end=" ")
    else:
        print("no", end=" ")
