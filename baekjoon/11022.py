# A+B - 8

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

T = int(input())

x = 0
for i in range(1, T+1):
    a, b = map(int, input().split())
    c = a+b
    print(f"Case #{x+i}: {a} + {b} = {c}")