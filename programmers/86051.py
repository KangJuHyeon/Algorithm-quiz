# 문제 접근
# 1~9 까지의 숫자 배열을 선언하고 포함되어 있는지 안되어있는지를 확인하면 된다.

def solution(numbers):
    answer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 0

    for i in range(len(answer)):
        if answer[i] not in numbers:
            result += answer[i]

    return result
print(solution([1, 2, 3, 4, 6, 7, 8, 0]))

# 다른사람의 풀이(1)
solution = lambda x: sum(range(10)) - sum(x)
print(solution([1, 2, 3, 4, 6, 7, 8, 0]))

# 다른사람의 풀이(2)
def solution(numbers):
    return 45 - sum(numbers)
print(solution([1, 2, 3, 4, 6, 7, 8, 0]))