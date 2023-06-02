# 코딩은 체육과목 입니다.

N = int(input())
answer = 'int'

for i in range(N // 4):
    answer = 'long ' + answer
print(answer)