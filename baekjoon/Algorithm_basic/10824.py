# 네 수(백준)

# 문제풀이(1)
numbers = list(map(int, input().split()))

for i in numbers:
    AB = str(numbers[0]) + str(numbers[1])
    CD = str(numbers[2]) + str(numbers[3])
    result = int(AB) + int(CD)
print(result)

# 문제풀이(2)
A, B, C, D = map(str, input().split())

AB = int(A+B)
CD = int(C+D)

print(AB+CD)