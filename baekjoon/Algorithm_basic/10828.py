# 문제 해결 방법
# 함수 사용, 조건문 사용 등을 사용하면 된다고 생각했다.
# sys를 사용하는 이유가 무엇인지 -> 시간초과가 나기 때문에 사용했다. 속도: sys.stdin.readline(4.5초) > input(12.5초)
# sys.stdin.readline 사용할 때 주의할 점, 개행문자(\n)가 같이 입력받아진다. 3을 입력했따면, 3\n이 저장된다. 개행문자 제거 해야된다.


# 문제풀이(1)
import sys
input = sys.stdin.readline
N = int(input()) # 테스트 케이스 갯수
stack = []

while True:
    test = input()[:-1]
    
    # push X: 공백 뒤에 숫자가 들어가야댐
    if test[:4] == 'push':
        stack.append(int(test[4:]))
    # 스택에서 가장 위에 있는 정수를 뺴고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif test == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    # 스택에 들어있는 정수의 개수를 출력한다.
    elif test == 'size':
        print(len(stack)) 
    # 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif test == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    # 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif test == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    else:
        break
    
# 문제풀이(2)
# 리스트로 스택 구현
def push(x):
    stack.append(x)

def pop():
    return stack.pop() if stack else -1

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1
    
import sys
N = int(input())
stack = []

for _ in range(N):
    text = sys.stdin.readline().rstrip().split()
    temp = text[0]
    if temp == "push":
        push(text[1])
    elif temp == "pop":
        print(pop())
    elif temp == "size":
        print(size())
    elif temp == "empty":
        print(empty())
    elif temp == "top":
        print(top())