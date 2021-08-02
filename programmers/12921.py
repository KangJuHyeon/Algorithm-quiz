# 문제 접근
# 소수란 정확히 무엇인지? 2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수
# 2부터 n까지의 모든 수를 확인해서 나누어 진다면 False, 안나누어진다면 True
# 반환하는 값은 리스트의 길이의 값을 반환해야 한다.
# 이중 포문을 돌려서 카운팅하는 방법으로 풀어도 될 것 같다.

# 수도코드(1)
def solution(n):
    for i in range(2, n+1):
        if n % i == 0:
            return False
    return True

# 수도코드(2)
# 이게 왜 안풀리는지는 이해가 안되는 것 같다.
def solution(n):
    answer = 0
    for i in range(n):
        cnt = 0
        for j in range(2, n+1):
            if n % j == 0:
                cnt += 1
        if i > 1 and cnt == 0:
            answer += 1
    return answer

# 문제풀이(1) 
# 에라토스테네스의 체 방식이지만, set형식이라 시간복잡도가 조금 떨어질 것 같다.
def solution(n):
	# 2부터 n까지의 숫자 배열 만들기
    num_set = set(range(2, n+1)) # 2 ~ 10까지라고 하면 {2, 3, 4, 5, 6, 7, 8, 9, 10}

    for i in range(2, n+1):
        if i in num_set: 
            num_set -= set(range(i*2, n+1, i)) # (i * 2)i가 2부터 시작하니까 (2x2=4, 3x2=6, 4x2=8, 5x2=10, (6x2=12) =>{2,3,5,7,9} 10+1, 2)

    answer = len(num_set)

    return answer

# 문제풀이(2)
# 수도코드(2)를 참조해서 다시 풀어보았다.
def solution(n):
    answer = 0
    for i in range(2, n+1):
        cnt = 0
        for j in range(2, i):
            if i % j == 0:
               cnt += 1
        if cnt == 0:
            answer += 1
        cnt = 0
    return answer 

# 이 문제를 풀고 나서의 기분(?) 혹은 느낀점
# 완전탐색이란 무엇인지, 소수 판별하는 방법에는 무엇이 있는지에 대해 궁금해졌고, 노션에 정리해 볼 생각이다.

# 에라토스테네스의 체 활용해서 문제풀이 해보기
import math

def solution(n):
    answer = [True] * (n + 1)
    result = 0

    for num in range(2, int(math.sqrt(n)+1)):
        if answer[num] == False:
            continue

        for i in range(num+num, n+1, num):
            answer[i] = False
            
    for i in range(2, n+1):
        if answer[i] == True:
            result += 1

    return result