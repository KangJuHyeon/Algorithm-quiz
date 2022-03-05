# 문제풀이(1)
T = int(input())

for i in range(T):
    text = input()[::-1]
    text = text.split()[::-1]
    print(" ".join(text))

# 문제풀이(2)
T = int(input())

for i in range(T):
    text = input()
    text += " "
    stack = []
    for j in text:
        # 공백이 아닐 때 stack에 넣고,
        if j!= " ":
            stack.append(j)
        # 공백이 맞다면 stack 리스트가 비어 있을 때까지 내용을 출력
        else:
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')

# 문제풀이(3)
import sys
T = int(sys.stdin.readline())
 
for _ in range(T):
  words = sys.stdin.readline().rstrip().split()
  print(words)
 
  for word in words:
    print(word)
    print(word[::-1], end=' ')
print()