# 합
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
# 1부터 n까지 합을 출력한다.

# 수도코드(1)
n = int(input())

for i in range(1, n+1):
    a = n + i
    
print(a)

# 문제풀이(1)
n = int(input())

answer = 0
for i in range(1, n+1):
    answer += i

print(answer)

# 문제풀이(2)
print(sum(range(1, int(input())+1)))