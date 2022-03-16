# pseudo-code(1)
def solution(s):
    # 열리면 count, 아니라면 제일 앞에 값을 빼서 뒤로 보낸다.
    # 0일때는 생각해준다.
    stack = list(s)
    count = 0
    
    for i in range(len(stack)):

        if stack[i] == "[":
            count += 1
        elif stack[i] == "(":
            count += 1
        elif stack[i] == "{":
            count += 1

        if stack[i] == "]":
            print(stack)
            stack.pop(0)
            print(stack)
            stack.append(stack[i])
            print(stack)
        if stack[i] == ")":
            print(stack)
            stack.pop(0)
            print(stack)
            stack.append(stack[i])
            print(stack)
        if stack[i] == "}":
            print(stack)
            stack.pop(0)
            print(stack)
            stack.append(stack[i])
            print(stack)

    return count
print(solution("[](){}")) # 3
print(solution("}]()[{")) # 2
print(solution("[)(]")) # 0
print(solution("}}}"))  # 0

# 문제풀이(1)
def solution(s):
    stack = list(s)
    count = 0

    for i in range(len(s)):
        box = []
        
        for j in range(len(stack)):
            if len(box) > 0:
                if box[-1] == '[' and stack[j] == ']':
                    print(box)
                    box.pop()
                elif box[-1] == '(' and stack[j] == ')':
                    print(box)
                    box.pop()
                elif box[-1] == '{' and stack[j] == '}':
                    print(box)
                    box.pop()
                else:
                    box.append(stack[j])
                    print(box)
            else:
                box.append(stack[j])
                print(box)
                
        if len(box) == 0:
            count += 1
        stack.append(stack.pop(0))
        print(stack)
 
    return count
print(solution("[](){}")) # 3
print(solution("}]()[{")) # 2
print(solution("[)(]")) # 0
print(solution("}}}"))  # 0