"""
시각

00시 00 분 00초 부터 N시 59분 59초까지의 시간중 3이 하나라도 포함된 횟수를 가져와라.

하루는 86400초, for문을 통해서 무조건 풀수있다.

"""

H = int(input())  # 시간

count = 0
for i in range(H + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
