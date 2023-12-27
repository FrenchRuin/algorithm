"""
큰수의 법칙

배열의 크기 N
숫자가 더해지는 횟수 M
특정 숫자 반복가능횟수 K

배열이 주어졌을때 가장 크게 나올 수 있는 수를 도출하자.
"""

"""
기본적인 방식 

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[n - 1]
second = arr[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

N = 5
M = 8
K = 3

위에서는 반복이 {6,6,6,5} , {6,6,6,5} 반복된다.

(K + 1) 의 크기의 배열이 반복됨
M / (K+1) 횟수만큼 (K+1)의 크기의 배열이 반복됨

제일큰 숫자의 반복은 M/(K+1) * K 가 된다.
그런데 나누어지지 않을경우에 나머지만큼 큰수가 반복된다.
즉, int(M/(K+1)) * K + M % (K + 1 ) 이 큰수가 반복된다.
큰수가 반복되는 횟수를 M에서 빼주면 두번째로 큰수를 만들어 주면 된다.
"""

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

count = int(m // (k + 1)) * k  # 큰수가 반복되는횟수
count += m % (k + 1)  # 나머지가 남았을경우를 대비해서 추가

arr.sort() # 정렬

result = 0
result += count * arr[n - 1]  # 큰수를 횟수만큼 곱해줌
result += (m - count) * arr[n - 2]  # 나머지횟수만큼 두번째로 큰수를 곱해준다.

print(result)
