# 문자열 붙여서 출력하기

# 1
str1, str2 = input().strip().split(' ')
print(str1 + str2)

# 2
print(''.join(input().strip().split(' ')))