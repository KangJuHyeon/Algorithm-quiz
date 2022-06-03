# 후위표기식

a = list(input()) # 후위 표기식 입력

stack = []
word = ''
for i in a:
    if i.isalpha(): # 알파벳인지 숫자인지 구분, 공백과 숫자를 포함하면 False
        word += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                word += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                word += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                word += stack.pop()
            stack.pop()

while stack:
    word += stack.pop()
print(word)