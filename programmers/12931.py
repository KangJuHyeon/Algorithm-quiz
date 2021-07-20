# 처음 문제 풀이
# for 문에 n을 순회하고 값을 더한다.
# 문자열로 변환해서 123 => "1", "2", "3"
# 위에 값을 더하면 끝

# 문제 풀이(1)
# 자릿수를 더하는 함수 : sum함수를 사용하여 풀이, 표현하면 매우 쉽다.

# 문제 풀이(2)
# n을 문자열로 바꿔서 answer에 저장하고,
# answer의 길이만큼 반복하는 i, 그동안 n의 i 인덱스 값을 result에 계속 더해준다.
# (더해줄 때에는 int로 바꿔줘야 에러도 안나고, 연산이 가능하다.)
# result 값 리턴

# 첫 번째 풀이(1) 안풀림
def solution(n):
    answer = 0
    for i in range(n):
        answer += i
    return answer

# 두 번째 풀이(2) 안풀림
def solution(n):
    answer = list(str(n))
    return int("".join(n))
# TypeError: can only join an iterable

# 세 번째 풀이(3) 통과 o
def solution(n):
    answer = str(n)
    result = 0
    for i in range(len(answer)):
        result += int(answer[i])
    return result

# 네 번째 풀이(4) 안풀림
def solution(n):
    answer = list(str(n))
    result = []
    for i in answer:
        result.append(i)
    return int("".join(result))

# 한 줄 요약 Best
    return sum(map(int, str(n)))