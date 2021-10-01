# 첫 번쨰 풀이
a, b = map(int, input().split(' '))
for i in range(b):            
    for j in range(a):        
        print('*', end='')
    print('')

# Best 풀이라고 합니다.
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

# 세 번째 풀이
a, b = map(int, input().split(' ')) 
star = '*' * a
for i in range(b):
    print(star)

# 네 번째 풀이
a, b = map(int, input().split(' ')) 
for i in range(b):
    print('*' * a)

# print() end=""와 sep="" 의 차이를 잘 알아볼 수 있었다. end=''는 123 붙여줄 수 있고, 띄어쓰기 하고 싶다면 ' ' 공백을 주면 된다. => 1 2 3
# sep=''는 print("010","1234","5678", sep="-") => 010-1234-5678 이런식으로 나올 수 있게 한다.
# 즉, sep(separation), 분리하여 출력한다.라고 생각하면 좋다. 위에를 보면 구분자를 선정하는 것이기 때문에 구분자는 "-"이 아이가 된다.
# print("H", "e", "l", "l", "o", "W", "o", "r", "l", "d", sep="@") => H@e@l@l@o@W@o@r@l@d