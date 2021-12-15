# 위클리 챌린지 : 피로도

# 문제이해
# 최소 필요 피로도와 소모 피로도를 다 사용해서 최대 탐헐할 수 있는 던전의 갯수를 카운팅해라.

# 문제 접근
# k에 있는 피로도가 2차원 배열에 있는 첫 번째 최소 필요 피로도를 빼줘야한다. (피로도 카운팅)
# 복사가 이상하다(?), 상자에 담아서 사용하는 필요성, 이유를 다시 깨달았다.
# count는 초기화되어야 한다, 다른 조합의 던전 카운팅을 세야한다.
# 다른 다양한 방식으로도 풀 수 있을 것 같다. ex)그래프, 큐, 힙
# 하지만 나는 조합으로 푸는 것이 가장 쉬울 것이라고 판단했다.

# 수도코드(1)
def solution(k, dungeons):
    count = 0 # 최대 던전 카운팅
    # Minimum Required Fatigue(최소 필요 피로도)
    # exhaustion fatigue(소모 피로도)
    print(dungeons)
    for fatigue in dungeons:
        MRF, EF = max(fatigue), min(fatigue)
        print(MRF, EF)
        if MRF <= k:
            MRF = max(fatigue)
        if EF < min(fatigue):
            EF = min(fatigue)
        k -= EF
        count += 1
        print(k)
    return count
print(solution(80,[[80,20],[50,40],[30,10]]))

# 문제풀이(1)
from itertools import permutations
def solution(k, dungeons):
    answer = 0
    dungeons = permutations(dungeons, len(dungeons))
    # print(dungeons)
    for permut in dungeons:
        MRF = k # 최소 피로도
        count = 0 # 최대 던전 카운팅
        for i in permut:
            if i[0] <= MRF:
                MRF -= i[1]
                count += 1
        
        if count > answer:
            answer = count
                
    return answer
print(solution(80,[[80,20],[50,40],[30,10]]))

# 문제풀이(2)
from itertools import permutations
def solution(k, dungeons):
    answer = []
    dungeons = permutations(dungeons, len(dungeons))
    for permut in dungeons:
        fatigue = k # 피로도
        count = 0 # 던전 카운팅
        for MRF, EF in permut:
            if MRF <= fatigue:
                fatigue -= EF
                count += 1
            else:
                break # 현재 피로도가 필요한 피로도보다 작다면 정지
        answer.append(count)
        print(answer)
        count = 0
    return max(answer) 
print(solution(80,[[80,20],[50,40],[30,10]]))