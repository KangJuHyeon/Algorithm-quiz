# 문제 접근
# x = 2 면 => [2, 4, 6, 8, 10] => n = 5
# 슬라이싱을 사용해서 [::2] 거리두기? 응 안대~ x 값이 있잔아
# 빈 배열에 자연수를 넣고, 그 배열을 리턴한다.
# n은 리스트안에 있는 값을 카운팅한 숫자?

# 수도코드
# 카운팅할 필요가없고, 그냥 n만큼 또는 n+1만큼 순회하고,
# 빈 배열에 (x * i) 값 또는 (x * (i+1))의 값을 넣어줘도 풀릴 것 같다.
def solution(x, n):
    answer = []
    for i in range(n+1):
        cnt = 0
        for j in range(x+1):
            answer += j
        if cnt == i:
            cnt += 1
    return answer

# 문제풀이(1)
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)
    return answer


# 문제풀이(2)
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x * (i+1))
    return answer

# Best 풀이
def solution(x, n):
    return [i * n + x for i in range(n)]