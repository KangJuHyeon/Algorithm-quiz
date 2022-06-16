# 내가 푼 문제 풀이(1)
from random import randint

def generate_numbers():
    numbers = []
    
    # 코드를 작성하세요.
    for i in range(3):
        result = randint(0, 9)
        if i not in numbers:
            numbers.append(result)
        
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

print(generate_numbers())

#################################################################################
#################################################################################

# 모범 답안
from random import randint

def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers