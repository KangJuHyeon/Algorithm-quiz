# 문제 접근
# 정렬 알고리즘, 앞 뒤 비교
# 문제를 읽고 다시 생각해보니 앞 뒤 비교 후 다 없어지면 1, 아니면 0 리턴

def solution(s):
    stack = []
    for i in range(len(s)):
        if stack == []:
            stack.append(s[i])
            print(stack)
        else:
            if s[i] == stack[-1]:
                stack.pop()
                print(stack)
            else: # 테스트 케이스 13번
                stack.append(s[i])

    if stack == []:
        return 1
    else:
        return 0
print(solution("baabaa"))
print(solution("cdcd"))

