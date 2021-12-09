# 문제접근
# x위치에서 y위치까지 가는 방법은 1이동, 2이동, 2이동, 1이동이 best라고 생각한다.
# 공간 이동장치의 안전성을 위해 y지점에 도착하기 직전의 이동거리는 반드시 1광년이라고 한다.

import math

T = int(input()) # 테스트케이스 갯수

for i in range(T):
    x, y = map(int, input().split())
    # x는 항상 y보다 작은 값을 갖는다.
    distance = y - x
    count = 0

    num = math.floor(math.sqrt(distance))   # n제곱 <= 거리 < (n+1)제곱일때 n제곱
    num_square = num ** 2   # n제곱의 제곱
    increase_num = math.sqrt(num_square)

    if distance > num_square + increase_num:
        count = 2 * num + 1
    elif distance > num_square and distance <= num_square + increase_num:
        count = 2 * num
    elif distance == num_square:
        count = 2 * num - 1

    if distance < 4:
        count = distance

    print(count)

# 다른사람의 풀이(1)
t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        print(count)
        move_plus += move  # count 수에 해당하는 move를 더함
        print (move_plus)
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
            print(move)
    print(count)