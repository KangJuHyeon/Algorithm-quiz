# 문제
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 
# 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

# 출력
# 각 테스트 케이스마다 점수를 출력한다.

# 수도코드(1)
n = int(input()) # 테스트 케이스의 개수

answer = [] # 빈 배열 => score를 나중에 담을 것
score = 0 # OX 카운팅
for i in range(n):
    judgment = input() # 문자열 입력
    if judgment[i] == "O": # 문자열 입력값이 "O"와 같다면
        score += 1
        answer += score # TypeError: 'int' object is not iterable => 반복문에 사용되는 변수가 정수인가 => 반복문을 사용할 수 있는가?
    elif judgment[i] == "X": # 문자열 입력값이 "X"와 같다면
        score += 0
    print(answer)
print(score)

# OOXXOXXOOO
# 1+1+0+0+1+0+0+1+1+1 = answer [1,1,0,0,1,0,0,1,1,1] X, [10] O 
# OOXXOXXOOO

# for문을 list, len 길이로 담아서 하나 더 한다. 이중 포문을 이용해 cnt 카운트를 세는 것처럼
# cnt로 카운팅해 누적 값을 담고, score로는 최종 점수를 담는다.

# 문제풀이(1)
n = int(input()) # 테스트 케이스의 개수

for i in range(n): # 정수로 들어간 반복문
    judgment = input() # 문자열 입력 값
    score = 0 # 수도코드처럼 리스트에 담지 않고, 정수로 담음
    cnt = 0 # OX 카운팅
    for j in list(judgment): # 리스트 안에 문자열 입력 값을 넣고 j로 추출
        if j == "O": # 문자열 입력값이 "O"와 같다면
            cnt += 1
            score += cnt
            print(cnt)
        elif j == "X": # 문자열 입력값이 "X"와 같다면
            cnt = 0
            print(cnt)
    print(score)

# 문제 풀이
# score는 누적될 점수의 변수, cnt는 점수를 누적할 때 사용되는 수이다.
# O인 경우 누적하면서 점수를 저장하고 X인 경우 cnt를 초기화 하고 0을 저장한다.