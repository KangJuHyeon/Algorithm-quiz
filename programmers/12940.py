def GCD(n, m): 
    R = n % m
    
    while(R > 0):
        n = m
        m = R
        R = n % m
    return m

def LCM(n, m):
    return n * m // GCD(n, m)

def solution(n, m):
    return [GCD(n, m), LCM(n, m)]


# 최대공약수는 유클리드 호제법으로 풀고, 최소공배수는 LCM 공식으로 함수를 나눠서 solution 함수에 리스트를 씌우고 함수를 불러와 최대공약수와 최소공배수를 풀었다.
# LCM 공식
# 최소공배수(LCM) = 두 자연수의 곱 / 최대공약수(GCD)
# 세 개의 자연수가 나올 때도 있다고 하니 공부를 하는 것이 좋겠다.
