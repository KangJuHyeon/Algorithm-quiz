# 내가 푼 문제 풀이(1)
def count_matching_numbers(list_1, list_2):
    # 코드를 작성하세요.
    lists = set(list_1) & set(list_2)
    return len(lists)

# 테스트
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))

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

# 테스트
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))