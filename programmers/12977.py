# 문제접근
# 3개의 다른 수를 더했을 때 소수가되는 수를 만든다.
# 에라토스테네스 체, 소수 판별식

from itertools import combinations

# 소수 판별 함수
def is_prime_num(num) :
    for i in range(2, num) :
        if num % i == 0 :
            return False
    return True

def solution(nums):
    answer = 0
    combo = list(combinations(nums, 3))
    for i in combo:
        print(i)
        if is_prime_num(sum(i)):
            answer += 1

    return answer
print(solution([1,2,3,4]))