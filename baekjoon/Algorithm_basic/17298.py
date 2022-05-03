# 오큰수

# 문제풀이(1)
N = int(input())
A = list(map(int, input().split()))

stack = []
result = []

for i in range(N):
    temp = A.pop()
    print("temp", temp)

    while stack:
        if temp < stack[-1]:
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
print(' '.join(result[::-1]))

# 문제풀이(2)
N = int(input())
A = list(map(int, input().split()))

stack = []
print(stack)
result = [-1] * N

for i in range(N):
    while stack and (stack[-1][0] < A[i]):
        tmp, idx = stack.pop()
        print(tmp, idx)
        result[idx] = A[i]
        print(result[idx])
        print(result)
    stack.append([A[i], i])
    print(stack)

print(*result)

# Unpacking 역할 (*)
ab_list = [1, 2]
print("a={}, b={}".format(*ab_list))