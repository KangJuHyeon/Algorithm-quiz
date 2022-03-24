# 문제 풀이(1)
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
    else:              # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print("NO")    # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데
        flag = 1       # TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
        break

if flag == 0:
    for i in answer:
        print(i)

# 문제 풀이(2)
count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력 
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)
         