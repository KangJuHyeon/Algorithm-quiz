# 문제 접근
# '('와 ')'가 연속적으로 나올 때 아니면 괄호가 닫힌 걸 어떻게 표현해야될 지
# 괄호가 안닫혔다면 False 다 잘 닫혀있다면 True
# 괄호가 열림을 카운팅, 닫힐때 -1을 해서 ()을 표현

# 수도코드(1)
# 수많은 고민 끝에 문제를 풀어버림
def solution(s):
    answer = True
    count = 0

    for i in s:
        if i == '(': # '('일 때 count + 1
            count += 1
            print(count)
        elif i == ')': # ')'일 때 count - 1
            count -= 1
            print(count)
            if count < 0: # 만약에 count가 0보다 작을 경우 괄호가 열리고 안닫혀있거나 시작을 안했을테니 False
                answer = False
        print(count)
    if count != 0: # count가 0과 다를 때 이것도 위에 조건과 같다 괄호가 안닫힘
        answer = False

    return answer
print(solution("()()")) # True
print(solution("(())()")) # True
print(solution(")()(")) # False
print(solution("(()(")) # False
print(solution(")(()))")) # False

# 문제풀이(1)
def solution(s):
    answer = True
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
            print(stack)
        else: # i == ')' 인 경우
            if stack == []: # 괄호 짝이 ')'로 시작하면 False를 반환
                answer = False
            else: # 빈 배열이 아닐경우
                stack.pop() # '('가 ')'와 짝을 이루려면 stack에서 '(' 하나 제거
                print(stack)

    if stack != []: # stack이 빈배열이 아닐 경우
        answer = False

    return answer
print(solution("()()")) # True
print(solution("(())()")) # True
print(solution(")()(")) # False
print(solution("(()(")) # False
print(solution(")(()))")) # False