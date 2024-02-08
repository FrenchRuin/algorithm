import random

# 1부터 45까지의 번호 생성
numbers = list(range(1, 46))

# 시뮬레이션 반복 횟수
simulations = 1000

# 각 번호가 나온 횟수를 저장할 딕셔너리 초기화
number_counts = {number: 0 for number in numbers}

# 시뮬레이션 수행
for _ in range(simulations):
    # 6개의 번호를 랜덤으로 추첨
    chosen_numbers = random.sample(numbers, 6)
    # 각 번호가 나온 횟수 증가
    for number in chosen_numbers:
        number_counts[number] += 1

# 각 번호의 확률 계산
total_draws = simulations * 6
probabilities = {number: count / total_draws for number, count in number_counts.items()}

# 결과 출력
for number, probability in probabilities.items():
    print(f"번호 {number}: {probability:.4f} 확률")