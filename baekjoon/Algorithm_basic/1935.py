# 후위 표기식2

n = int(input()) # 피연산자의 개수 입력
a = input() # 후위 표기식 입력
alpha = [0] * n

for i in range(n):
    alpha[i] = int(input()) # 피연산자 값 받기

stack = []

for i in a:
    if 'A' <= i <= 'Z':
        stack.append(alpha[ord(i) - ord('A')])
    else:
        str1 = stack.pop()
        str2 = stack.pop()

        if i == '+':
            stack.append(str2+str1)
        elif i == '-':
            stack.append(str2-str1)
        elif i == '*':
            stack.append(str2*str1)
        elif i == '/':
            stack.append(str2/str1)
print('%.2f' %stack[0])