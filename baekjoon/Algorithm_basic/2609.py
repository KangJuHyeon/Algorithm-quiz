# 최대공약수와 최소공배수(백준)
a, b = input().split()
a = int(a)
b = int(b)

# a는 최대공약수
# b는 최소공배수

def gcd(x, y):

    while y:
        x, y = y, x % y
    
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

print(gcd(a, b))
print(lcm(a, b))