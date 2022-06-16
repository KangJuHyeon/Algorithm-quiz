# 내가 푼 문제 풀이(1)
def count_matching_numbers(numbers, winning_numbers):
    # 지난 과제의 코드를 붙여 넣으세요.
    lists = set(numbers) & set(winning_numbers)
    return len(lists)

def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    answer = 0
    bouns_number = winning_numbers[-1:]
    
    # print(count_matching_numbers(numbers, winning_numbers[:-1]))
    if count_matching_numbers(numbers, winning_numbers[:-1]) == 6:
        answer = 100000000
    elif count_matching_numbers(numbers, winning_numbers[:-1]) == 5 or count_matching_numbers(numbers, winning_numbers) == bouns_number:
        answer = 50000000
    elif count_matching_numbers(numbers, winning_numbers) == 5:
        answer = 1000000
    elif count_matching_numbers(numbers, winning_numbers) == 4:
        answer = 50000
    else:
        answer = 5000
    
    return answer

# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))

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


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count


def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0