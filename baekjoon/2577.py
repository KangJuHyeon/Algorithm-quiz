# 문제
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

# 입력
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

# 문제 접근
# a * b * c = 17037300
# [17037300]이 나올때 어떻게 정수를 나누지? 문자열로 나눠야하나?
# 숫자의 개수를 세야된다? count함수 사용해서 출력

# 문제풀이(1) 주석, line 22, 25를 제거하고 제출하니 통과됐다.
answer = []

while True:
    a = int(input())
    b = int(input())
    c = int(input())
    result = a * b * c
    answer = list(map(int, str(result))) #10보다 큰 숫자는 간혹 숫자를 쪼개야하는 경우가 생긴다. 그럴 때 유용하게 사용할 수 있다 
    # answer.append(result)
    break
    # A × B × C = 150 × 266 × 427 = 17037300
print(answer) # [17037300] => [1, 7, 0, 3, 7, 3, 0, 0]
print(answer.count(0))
print(answer.count(1))
print(answer.count(2))
print(answer.count(3))
print(answer.count(4))
print(answer.count(5))
print(answer.count(6))
print(answer.count(7))
print(answer.count(8))
print(answer.count(9))

# 다른사람 문제 풀이(1)
a = int(input())
b = int(input())
c = int(input())

d = list(map(int, (str(a * b * c))))

for i in range(10):
    print(d.count(i))