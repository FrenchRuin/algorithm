"""
DP 1장

1로 만들기

1. 5로나눈다
2. 3으로 나눈다.
3. 2로 나눈다.
4. x에서 1을뺀다
를 반복했을때, 1로 만들수 있는 연산 최솟갓
"""

N = int(input())

dp = [0] * 30001  # 초기화

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[N])
