# 내가 푼 문제 풀이(1)
from random import randint

def generate_numbers(n):
    # 코드를 작성하세요.
    answer = []

    for i in range(n):
        random_number = randint(1, 45)
        answer.append(random_number)
    
    return answer
    
print(generate_numbers(6))

#################################################################################
#################################################################################

# 모범 답안
from random import randint

def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers

# 예시 결과 출력
print(generate_numbers(6))