# 문제 읽기
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 리턴하는 함수를 작성하라.

# 입출력 예
# prices = [1, 2, 3, 2, 3] return = [4, 3, 1, 1, 0]

# 문제 접근
# 주식 가격 문제는 문제 이해부터가 쉽지 않았다.
# 문제를 이해하고 나서 식을 공책에 적어봤다.
# answer[스택 저장된 시간] = 최종 시간 - 스택 저장된 시간
# answer[4] = 4-4 = 0
# answer[3] = 4-3 = 1
# answer[1] = 4-1 = 3
# answer[0] = 4-0 = 4
# 파이썬은 answer = [0] * 개수 하면 개수만큼 0으로 초기화된 리스트가 만들어 진다.

# 처음 수도코드(1)
def solution(prices):
# count ? 띵킹
# 1초일때 answer.append(i+3) [4,]
# 2초일때 answer.append(i+1) [4,3]
# 3초일때 answer.append(i-2) [4,3,1]
# 4초일때 answer.append(i-i) [4,3,1,?,0]
    answer = []
    count = 0
    for i in range(len(prices)):
        print(i)
        # 배열의 0일 때를 생각해야된다.
        if i == int(0):
            answer.append(i+4)
        elif i == int(1):
            answer.append(i+2)
        elif i == int(2):
            answer.append(i-1)
        elif i == int(3):
            answer.append(i-2)
        elif i == int(4):
            answer.append(i-i)
        print(answer)

    return answer
print(solution([1, 2, 3, 2, 3]))

# 문제 풀이(1) LIFO stack 풀이
def solution(prices):
    n = len(prices)
    answer = [0] * len(prices) # [0, 0, 0, 0, 0] 이렇게 나옴
    stack = [] # 시간을 담을 Stack 선언
    for i in range(n):
        print(i)
        print(prices[i])
        # stack이 비지 않고, 가장 마지막 원소인 top의 값이 현재 주식 가격보다 비싸다면
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
            print(answer[top])
            print(answer)
        # 스택에 현재 시간 i 저장 0, 1, 2, 3, 4
        stack.append(i)
        print(stack)
    
    # 만약 stack이 남아있다면, 스택이 빌 때까지 다음 반복
    while stack:
        # 1. 스택에서 마지막에 저장된 시간 top을 꺼낸다.
        # 2. answer[top]에 가장 마지막 시간 n - i 에서 top을 뺀 시간 저장
        print(stack)
        top = stack.pop()
        answer[top] = n - 1 - top
        print(answer[top])
        print(answer)
    
    return answer
print(solution([1, 2, 3, 2, 3]))

# 문제 풀이(2) FIFO Queue 풀이
from collections import deque

def solution(prices):
    n = deque(prices)
    print(n)
    answer = []
    
    while n:
        prices = n.popleft() # [1, 2, 3, 2, 3] 왼쪽부터 pop해서 prices에 담는다.
        time = 0 # 초 카운팅
        for i in n: # 앞에 원소가 하나 빠져서 2부터 시작
            print(i)
            print(prices)
            time += 1
            print(time)
            if prices > i:
                break
        answer.append(time)
        print(answer)
    
    return answer
print(solution([1, 2, 3, 2, 3]))

# 다른 사람이 푼 Best 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer