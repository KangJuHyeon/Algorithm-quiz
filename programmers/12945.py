# 문제 읽기
# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1이상의 n에 대하여 F(n) = F(n-1)+F(n-2)가 적용되는 수이다.

# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# F(n) = F(n-1) + F(n-2) = (n-1) + (n-2) = n

# 2이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수를 만들어라.

# 문제 접근
# (n-1) + (n-2) => 곧 F(n)의 값이다.
# 재귀함수? for문? 메모이제이션 기법?

# 수도코드(1) 
# 런타임 에러
def solution(n):
    if n < 2:
        return n
    else:
        return solution(n-1) + solution(n-2)
print(solution(5))

# 수도코드(2)
# 런타임 에러
def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return solution(n-1) + solution(n-2)
print(solution(5))

# 수도코드(3)
def solution(n):
    answer = [0,1]

    for i in range(2, n+1):
        answer.append(answer[i-1] + answer[i-2])
        # print(answer)

    return answer[-1]
print(solution(5))

# 문제 풀이(1)
# 문제를 잘 읽어봐야한다.
def solution(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
        print(a)
        # print(b)
    return a % 1234567
print(solution(5))