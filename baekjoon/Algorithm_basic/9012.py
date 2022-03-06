# 문제풀이(1)
T = int(input())

for i in range(T):
    text = input()
    stack = []

    for j in text:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                stack.append(")")
                break

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")