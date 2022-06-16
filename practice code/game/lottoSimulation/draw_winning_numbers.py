# 문제풀이(1)
from random import randint

def generate_numbers(n):
    # 지난 과제의 코드를 붙여 넣으세요.
    answer = []

    for i in range(n):
        random_number = randint(1, 45)
        answer.append(random_number)
    
    answer.sort()
    return answer


def draw_winning_numbers():
    # 코드를 작성하세요.
    bouns_number = generate_numbers(6) + generate_numbers(1)
    
    return bouns_number

print(draw_winning_numbers())

# 문제풀이(2)
from random import randint

def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]