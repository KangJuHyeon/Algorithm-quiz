# 문제 접근을 완료하고 만들어 본 수도코드 => 통과는 되지만 제출이 안되는 코드
def solution(a, b):
    answer = 0
    for i in range(a, b+1):
        for j in range(1, i+1):
            if a == b:
                return i
            else:
                answer += 1
    if a > b: # 
        return sum([i for i in range(b, a+1)])
    return answer

# 문제풀이(1)
def solution(a, b):
    answer = 0
    for i in range(a, b+1):
        if a == b:
            return i
        else:
            answer += i
    
    for i in range(b, a+1):
        answer += i
    return answer

# 문제풀이(2) sum함수 사용
def solution(a, b):
    return sum(range(a, b+1) if a <= b else range(b, a+1))

# 문제 접근
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하라.
# 이중 포문을 이용해서 값을 추출하자.
# 값이 같은 경우와 a가 클 경우에는? 어떡하지? => 그대로 if 조건문을 만들면 된다.
# sum 함수를 사용? => 가능하다.
