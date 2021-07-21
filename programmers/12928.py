# 문제풀이(1)
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if(n % i == 0):
            answer += i
    return answer

# 문제풀이(2) sum 함수
def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])


# 처음 문제 풀이
# 1부터 입력받은 수 n까지 순회하여 n을 나눠서 0일 경우...
# 약수를 모두 더한 값을 담을 변수 지정
# for문을 사용해서 약수 구하기
# sum함수를 사용해서 풀이