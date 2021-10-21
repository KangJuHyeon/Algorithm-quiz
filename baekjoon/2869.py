# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

# V미터 막대
# A미터 올라갈 수 있다.
# B미터 미끄러진다.

# 2 1 5 입력값이라면
# 1일 => 2-1 = 1, 2일 => 1 + (2-1) = 2 3일 => 2 + (2-1) = 3이 되지만
# 4일 차는 3 + 2 = 5로 밤에 미끄러지지 않고 정상에 도달할 수 있다. 정상에 올라가면 다시 미끄러지면 안된다.

A, B, V = map(int, input().split())
# (1 ≤ B < A ≤ V ≤ 1,000,000,000)

count = 0 # 올라가는데 걸리는 일수(카운팅)
height = 0 # 올라간 높이

while True:
    count += 1
    height += A # A를 넣어줌으로써 얼마나 올라갔는지 확인
    if height == V:
        print(count)
        break
    height -= B
print(count)

# 다른사람의 풀이
import math
a, b, v = map(int, input().split())

answer = math.ceil((v-b) / (a-b))

print(answer)


