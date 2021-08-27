# 문제
# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.


# 문제풀이(1)
def solve(n):
    a = 0
    for i in n:
        a += i
    return a

print(solve([10]))

# 문제풀이(2)
def solve(n):
    return sum(n)
print(solve([225]))