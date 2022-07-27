# 소수 구하기(백준)

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)

# 문제풀이(2)
M, N = map(int,input().split())

for i in range(M,N+1):
    if i == 1: # 1은 소수가 아니므로 제외
        continue
    for j in range(2,int(i**0.5)+1):
        if i % j == 0: # 약수가 존재하므로 소수가 아님
            break   # 더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)