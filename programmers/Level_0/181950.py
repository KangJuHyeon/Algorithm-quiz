# 문자열 반복해서 출력하기

a, b = input().strip().split(' ')

for i in range(int(b)):
    print(a, end= "")



# 2
a, b = input().strip().split(' ')
b = int(b)

result = a * b
print(result)