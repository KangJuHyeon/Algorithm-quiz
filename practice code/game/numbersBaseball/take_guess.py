# 내가 푼 문제 풀이
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    # 코드를 작성하세요.

    i = 1
    while True:
        number = int(input(f"{i}번째 숫자를 입력하세요: "))

        if number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            number = int(input(f"{i}번째 숫자를 입력하세요: "))
        if number > 10:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.") 
            number = int(input(f"{i}번째 숫자를 입력하세요: "))
        if len(new_guess) >= 3:
            break
        
        new_guess.append(number)
        i += 1

    return new_guess

print(take_guess())

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


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        new_num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))

        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_num)

    return new_guess