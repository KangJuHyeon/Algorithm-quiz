import sys
input = sys.stdin.readline
n = int(input())
stack = []
answer = []
flag = 0
count = 1

for i in range(0, n):
    put = int(input())
    # print(put)
    
    while count <= put:
        stack.append(count) # 입력한 수를 만날 때 까지 오름차순으로 push
        answer.append("+")
        count += 1
    # 입력한 수를 만나면 while문 탈출. 즉 count = put일 때 까지 while문을 돌아 스택을 쌓는다.

    if stack[-1] == put:
        stack.pop() # stack의 Top이 입력한 숫자와 같다면
        answer.append("-") # 스택의 TOP을 꺼내 수열을 만들어 준다.
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)
         