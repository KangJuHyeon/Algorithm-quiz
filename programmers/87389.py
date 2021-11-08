def solution(n):
    for x in range(2, n):
        if n % x == 1:
            return x
    return n
print(solution(10)) # 3
print(solution(12)) # 11