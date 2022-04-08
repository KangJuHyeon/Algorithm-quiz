# (조건1)k점(k는 1~10사이의 자연수)점을 어피치가 a발 맞혔고 라이언이 b발을 맞혔을 경우 더 많은 화살을 k에 맞힌 선수가 k점을 가져갑니다.
# (조건1)단, a = b일 경우는 어피치가 k점을 가져갑니다.
# * 어피치가 10점을 2발 맞혔고 라이언도 10점을 2발 맞혔을 경우 어피치가 10점을 가져갑니다.
# * 다른 예로, 어피치가 10점을 0발 맞혔고 라이언이 10점을 2발 맞혔을 경우 라이언이 10점을 가져갑니다.

# (조건2)k점을 여러발 맞혀도 k점 보다 많은 점수를 가져가는 게 아니고 k점만 가져가는 것을 유의하세요.
# (조건3)또한 a = b = 0 인 경우, 즉, 라이언과 어피치 모두 k점에 단 하나의 화살도 맞히지 못한 경우는 어느 누구도 k점을 가져가지 않습니다.

# (조건4)최종 점수가 높은 점수가 우승자, 단, 최종 점수가 같을 경우 어피치를 우승자로 결정합니다.

# 문제: 라이언은 어피치를 가장 큰 점수 차이로 이기기 위해서 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지를 구하려고 합니다.

# 화살의 개수를 담은 자연수 n
# 어피치가 맞힌 과녁 점수의 개수를 10점부터 0점까지 순서대로 담은 정수 배열 info
# (조건5) 라이언이 우승할 수 없는 경우(무조건 지거나 비기는 경우) [-1]을 리턴해주세요.

# 라이언 점수를 어떻게 표현해야 할까?

# 수도코드(1)
def solution(n, info):
    answer = []
    score = 0
    scoreBoard = { 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2, 1: 1, 0: 0}
    for key, value in enumerate(info):
        print(key, value)
        if key == 0 and value > 0:
            score += 10
        elif key == 1 and value > 0:
            score += 9
        elif key == 2 and value > 0:
            score += 8
        elif key == 3 and value > 0:
            score += 7
        elif key == 4 and value > 0:
            score += 6
        elif key == 5 and value > 0:
            score += 5
        elif key == 4 and value > 0:
            score += 4
        elif key == 3 and value > 0:
            score += 3
        elif key == 2 and value > 0:
            score += 2
        elif key == 1 and value > 0:
            score += 1
        elif key == 0 and value >= 0:
            score += 0   
    print(score)      
    return answer
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) # [0,2,2,0,1,0,0,0,0,0,0]

# 문제풀이(1)
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [0 for i in range(11)]
    win = False
    max_num = 0 # 라이언이 이길 때 가장 큰 점수 차이
    # 1. 중복 조합을 이용해 라이언의 점수를 만든다.
    for res in list(combinations_with_replacement(range(0, 11), n)):
        now = [0 for i in range(11)]
        for j in res:
            now[10 - j] += 1
        lion = 0
        apeach = 0
        # 2. 라이언 점수와 어피치 점수를 비교한다.
        for k, (l, p) in enumerate(zip(now, info)):
            if l == p == 0:
                continue
            if p >= l:
                apeach += (10 - k)
            elif l > p:
                lion += (10- k)
        # 3. 총 점수를 비교해 라이언이 큰 경우 결과를 업데이트 해준다.
        if lion > apeach:
            win = True
            if (lion - apeach) > max_num:
                max_num = lion - apeach
                answer = now
    
    # (조건5) 라이언이 우승할 수 없는 경우(무조건 지거나 비기는 경우) [-1]을 리턴해주세요.
    if not win:
        return [-1]

    return answer
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) # [0,2,2,0,1,0,0,0,0,0,0]
