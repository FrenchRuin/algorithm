"""
곱하기 혹은 더하기

그냥 0나오면 더하고 나머지는 다 곱하면 그만이다.


"""

input_data = input()

answer = int(input_data[0])

for i in range(1, len(input_data)):
    num = int(input_data[i])
    if num <= 1 or answer <= 1:
        answer += num
    else:
        answer *= num

print(answer)
