# 문제접근
# 순간이동으로 최대한 많이 이동해야 건전지 사용량이 최소가 된다.
# 현재 위치부터 0까지 도달하는 방법 : 역산

# 문제풀이(1)
def solution(n):
    ans = 0
    while n > 0:
        # 현재위치 % 2
        ans += n % 2
        print(ans)
        n = n // 2

    return ans
print(solution(5))    # 2 
print(solution(6))    # 2
print(solution(5000)) # 5

# 문제풀이(2)
def solution(n):
    ans = 0
    # 0이 될 때까지 반복
    while n > 0:
        # n값이 0이 될 때까지 2로 나눈 몫과 나머지를 구하고
        x, y = divmod(n, 2)
        n = x
        # y가 0이 아닐경우, 나머지가 1이면 카운팅
        if y != 0:
            ans += 1

    return ans
print(solution(5))    # 2 
print(solution(6))    # 2
print(solution(5000)) # 5

# 다른사람의 풀이(1)
def solution(n):
    return bin(n).count('1')