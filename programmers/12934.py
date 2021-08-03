# 정수 제곱근을 판별하라. 어떻게?
# 양의 정수 n의 값이 제곱인지 아닌지를 판별하라 True이면 제곱값의 +1 하여 리턴,
# 만약 False라면 -1을 리턴하라.

# 문제 접근
# math 라이브러리를 사용하여 풀이를 진행해보자.
# pow() 내장 함수를 이용해도 풀릴 수는 있을 것 같다.
# 제일 중요한 파이썬에서 제곱근을 어떻게 구하는지부터 알아봐야할 것 같다.

# 제곱근을 구하는 여러가지 방법
# n ** 5
# pow(n, 0.5)
# math.sqrt(n)

# 정리
# 제곱근을 구하려면 import math 를 통해서 모듈을 임포트하고 math.sqrt() 함수를 통해서 제곱근을 구할 수 있다.
# int() 를 통해서 주어진 인수를 정수로 변환할 수 있다.
# pow(4,2)과 4 ** 2 (=16) 을 통해서 제곱 연산을 할 수 있다.
# 반대로 pow(4,0.5)과 4 ** 1/2 (=2) 을 통해서 제곱근을 구할 수 있다.

# 문제 풀이(1) 제곱근의 기본적인 계산 활용
def solution(n):
    answer = n ** (1/2)
    if answer % 1 == 0: # 만약 answer가 양의 정수라면 1과 나누어 떨어져 0이 될 수 있다. 그렇다면 양의 정수라면 ex) (11+1) ** 2의 값을 리턴
        return (answer + 1) ** 2
    else:
        return -1

# 문제 풀이(2) math 라이브러리 활용
import math
def solution(n):
    answer = math.sqrt(n)
    if answer % 1 == 0:
        return (answer+1) ** 2
    else:
        return -1

# 문제 풀이(3) math.pow() 활용
import math
def solution(n):
    answer = math.pow(n, 0.5)
    if answer % 1 == 0:
        return (answer+1) ** 2
    else:
        return -1

# 문제 풀이(4) 조건문을 바꿔서 풀이
import math
def solution(n):
    answer = math.pow(n, 0.5)
    if answer == int(answer): # 만약 answer가 int(answer)와 같다면 ex) (11+1)값의 2의 제곱 값을 리턴하라.
        return (answer+1) ** 2
    else:
        return -1