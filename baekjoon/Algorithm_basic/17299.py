# 오등큰수

N = int(input())
A = list(map(int, input().split()))

stack = []
result = []

for i in range(N):
    temp = A.pop()
    print("temp", temp)

    while stack:
        if temp > stack[-1]:
            result.append(str(stack[-1]))
            print("result", result)
            break
        else:
            stack.pop()
            print("stack", stack)
    if stack == []:
        result.append(str(-1))
        print("result", result)
    
    stack.append(temp)
    print("stack", stack)
print("정답", ' '.join(result[::-1]))

# 문제풀이(2)
from collections import Counter
import sys 

sys.stdin = open("/Users/kangjuhyeon/Documents/my-project/Algorithm-quiz/baekjoon/Algorithm_basic/input.txt", "r")
N = int(sys.stdin.readline())
print("N", N)
A = list(map(int, sys.stdin.readline().split()))
print("A", A)
count = Counter(A)
result = [-1] * N
stack = [0]
print(stack)

for i in range(1, N):
    while stack and count[A[stack[-1]]] < count[A[i]]:
            result[stack.pop()] = A[i]
    stack.append(i)

print(*result)