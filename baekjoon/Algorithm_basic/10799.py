# 쇠막대기

# 조건
# 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있습니다.
# 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓습니다.
# 각 쇠막대기를 자르는 레이저는 적어도 하나 존재합니다.
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않습니다.

# 문제 궁금점
# 쇠막대기를 어떤식으로 표현하는 것일까? 잘보면 첫 번째 괄호 기준으로 제일 큰 쇠막대기 생성
# "()" 이것은 레이저 발사 방향, 시작점, 레이저를 표현

bracket = list(input())

stack = [] 
stick = 0 # 쇠막대기 원본
count = 0 # 원본이 잘린 갯수
for i in range(len(bracket)):
    temp = bracket.pop(0)
    print("막대기", temp)
    
    # 쇠막대기의 시작이라면?
    if temp == "(":
        stick += 1
        print("stick", stick)
        count += 1
        print("count", count)
    # 레이저인지, 막대 끝인지 확인
    else:
        # 쇠막대기의 끝이 아니라, 레이저라면
        if stack[-1] == "(":
            print("stack", stack)
            stick -= 1
            print("stick", stick)
            count -= 1
            print("count", count)
            count += stick
            print("count", count)
        # 쇠막대기의 끝이라면
        else:
            print("stack", stack)
            stick -= 1
            print("stick", stick)
    stack.append(temp)
print(count)

# 문제 풀이(2)
from typing import List
class Solution:
    def solve(self, args):
        answer = list(args)
        stack = []
        stick = 0
        count = 0
        for i in range(len(answer)):
            temp = answer.pop(0)
            if temp == "(":
                stick += 1
                count += 1
            else:
                if stack[-1] == "(":
                    stick -= 1
                    count -= 1
                    count += stick
                else:
                    stick -= 1
            stack.append(temp)
        return count
    # print(solve("()(((()())(())()))(())"))
    # print(solve("(((()(()()))(())()))(()())"))

    def solve_two(self, str):
        inputStr = list(str)
        stack = []
        count = 0
        
        for i in range(len(inputStr)):
            if inputStr[i] == "(":
                stack.append("(")
            else:
                if inputStr[i-1] == "(":
                    stack.pop()
                    count += len(stack)
                else:
                    stack.pop()
                    count += 1
        return count
        
if __name__ == '__main__':
    print(Solution().solve(input()))
    # print(Solution().solve_two(input()))
# print(Solution().solve("()(((()())(())()))(())"))
# print(Solution().solve("(((()(()()))(())()))(()())"))
# print(Solution().solve_two("()(((()())(())()))(())"))
# print(Solution().solve_two("(((()(()()))(())()))(()())"))