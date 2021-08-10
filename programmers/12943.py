# 문제 풀이
# 입력된 수가 3(홀수)이면 3 x 3 + 1 = 10
# 입력된 수가 6(짝수)이면 6 % 2 = 3
# 위에 숫자의 결과가 1이 될 때까지 반복해준다.
# 위에 작업이 500번 반복된다면 -1을 리턴하라.

# 문제 접근
# 카운트를 세서 반복을 세야하나?

# 수도코드(1)
def solution(num):
    answer = 0
    for i in range(1, num+1):
        if num % 2 == 0: # 짝수일 때
            answer += num % 2
            cnt += 1
        elif num % 1 == 0: # 홀수일 때
            answer += (n * 3) + 1
            cnt += 1
        elif cnt <= 500: # 500번 반복했을 경우
            return -1
        if answer != 1:
            break
    return answer

# 문제풀이(1) 통과가 안댐...
def solution(num):
    answer = 0
    for i in range(500):
        if num % 2 == 0: # 짝수일 때
            num = num / 2
        else: # 홀수일 때
            num = (num * 3) + 1
        if num == 1: # 만약 num이 1과 같다면 횟수(i)를 리턴
            return i + 1
        
    return -1

# 문제풀이(2) 통과가 된다.
def solution(num): 
    answer = 0 # 반복 카운팅
    for i in range(500): 
        if num % 2 == 0: # 짝수일 때
            num = num / 2 
            answer += 1 
        if num == 1: # num이 1과 같을 때 멈춘다. loop를 빠져나온다.
            break 
        if num % 2 != 0: # 홀수일 경우
            num = (num*3)+1 
            answer += 1 
        if num == 1: # num이 1과 같을 때 멈춘다. loop를 빠져나온다.
            break 
        if answer > 500: # 반복 카운팅 수가 500번을 반복하게 된다면 -1을 리턴
            return -1
    return answer

# 다른사람의 문제풀이(1)
def collatz(num):
    answer = 0
    while num!=1:
        if num%2==0:
            num=num/2
        else:
            num=3*num+1
        answer=answer+1

        if answer>=500:
            return -1

    return answer
print(collatz(6))

# 다른사람의 문제풀이(2) 
# 코드가 직관적이고 좋은 것 같다.
def collatz(num):
    answer = 0
    while answer < 500: # 반복 카운팅이 500보다 작다면
        answer += 1
        if num % 2 == 0: # 짝수일 때
            num = num / 2
        else: # 홀수일 때
            num = (num * 3) + 1
        if num == 1: # num이 1과 같다면 loop out
            break
    if answer == 500: # 만약 반복 카운팅이 500과 같다면 -1을 담는다.
        answer = -1

    return answer

# Best 풀이
# 삼항 연산자를 이용하여 잘 풀었다.
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1

# 내 수도코드와 제일 비슷한 다른사람의 풀이(3)
def collatz(num):
    for i in range(0,502): # 0부터 501까지 반복
        if i > 500: # i가 500보다 클 경우 -1을 리턴한다.
            return -1
        else: # i가 500보다 작을 경우
            if num == 1: # num이 1과 같다면 그대로 반복 횟수를 리턴한다.
                return i
            elif num != 1: # 또는 num이 1과 같지않다면
                if num % 2 == 0: # 짝수일 경우
                    num = num / 2 
                else: # 홀수일 경우
                    num = num * 3 + 1