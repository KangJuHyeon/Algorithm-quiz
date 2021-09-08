# 문제 읽기
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
# 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서,
# n개의 수의 최소공배수는 n개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수를 작성하시오.

# arr = [2,6,8,14], result = 168
# arr = [1,2,3], result = 6

# 문제 접근
# 2 * 1 * 3 * 4 * 7 = 168
# 1 * 2 * 3 = 6
# GCD
# LCM = x * y // GCD(x, y)

# 수도코드(1) 및 문제 풀이(1)
def GCD(n,m): # 최대공약수
    if n % m == 0: # n의 값이 2,6,8,14를 0으로 나눴을 때
        return m # arr의 i값을 리턴
    else:
        # print(GCD(m, n % m))
        return GCD(m, n % m) 

def LCM(n, m): # 최소공배수 구하기
    return n * m // GCD(n, m)

def solution(arr):
    answer = arr[0]

    for i in arr: # m의 값을 추출
        answer = LCM(answer, i)
    return answer
print(solution([2,6,8,14]))

# 다른사람의 풀이(1)
# math 라이브러리의 gcd 함수를 쓰는 것
from math import gcd

def solution(arr):      
    answer = arr[0]
    for n in arr:
        answer = n * answer / gcd(n, answer)

    return answer
print(solution([1,2,3]))