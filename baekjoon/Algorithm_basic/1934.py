# 최소공배수(백준)
import math
T = int(input())

def lcm(x, y):
    return x * y // math.gcd(x, y)

for i in range(T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    print(lcm(A, B))