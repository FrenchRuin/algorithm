"""
1 이 될때까지...

1. N 에서 1을뺀다.
2. N을 K로 나눈다.

N 이 1이 될때까지의 최소횟수를 가져간다.
"""

N, K = map(int, input().split())

result = 0

while True:
    target = (N // K) * K
    result += (N - target)
    N = target

    if N < K:
        break

    result += 1
    N //= K

result += (N - 1)
print(result)
