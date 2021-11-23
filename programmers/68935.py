# 문제접근
# 2진수, 8진수, 10진수, 16진수로 쉽게 변환할 수 있도록 내장함수가 포함되어 있다
# 하지만 3진수나 4진수와 같이 다른 진수로 변환하고자 한다면 직접 구현을 할 수 밖에 없다.
# 1) divmod() : 몫과 나머지를 같이 반환해주는 함수
# 2) int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌
# python의 int 함수는 진법 변환을 지원합니다.

# 문제풀이(1)
def solution(n):
    answer = ''
    while n > 0:
        i, j = divmod(n, 3)
        answer += str(j)
        n = i
        # print(n)
        print(answer)
    return int(answer, 3)
print(solution(45))
print(solution(125))

# 문제풀이(2)
def solution(n):
    answer = ''
    while n:
        answer += str(n % 3)
        n = n // 3
    return int(answer, 3)
print(solution(45))