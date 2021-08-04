# 문제
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 한다.
# 10 = 1+0 = 1  : 10 % 1 = 10
# 12 = 1+2 = 3  : 12 % 3 = 4
# 11 = 1+1 = 2  : 11 % 2 = 안나누어짐(소수)

# 문제 접근
# 자릿수를 더한 값과, 그 값과 x가 나누어 떨어지는 함수를 리턴하라.
# 문자열로 바꾸고 [0][1]의 값을 더하고, 그 값을 int형으로 변환해서 풀어보자.
# sum 함수를 사용할 수도? 있을 것 같다.

# 수도코드
def solution(x):
    answer = str(x)
    result = 0

    for i in range(len(answer)):
        result += int(answer[i])
    if x % result == 0:
        return result

# 문제풀이(1)
def solution(x):
    answer = str(x)
    result = 0
    
    for i in range(len(answer)):
        result += int(answer[i])

    if x % result == 0:
        return True
    else:
        return False

# Best 풀이 정리 sum함수 활용하기
def solution(x):
    return False if x % sum([int(i)for i in str(x)]) != 0 else True