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