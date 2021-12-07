# 문제이해
# N / stages = 실패율
# stages의 1, 2, 3, 스테이지 별 통과못한 사람의 배열이다.
# 그럼 1번 스테이지 실패율 : 1/8
# 2번은 스테이지 실패율 : 3/7 이런식으로 나온다.

# 문제접근
# 그렇다면 실패율을 구하면 되니까 
# 1번 스테이지 실패율을 구하면서 stage의 길이를 1번 실패한 사람만큼 빼는 형식으로 구한다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의한다.

# 문제 해결 과정 정리
# 수도코드를 정리 못했음, 처음엔 변수명 정리가 잘 안되서 매우 복잡했음
# 변수명 정리를 통해 코드 가독성을 높이려고 노력했음

# 1. 실패율 = N스테이지에 도달하지 못한 인원들(count) / N스테이지에 도달한 수(length)
# 2. 스테이지에 도달한 유저가 없는 경우 0, 있다면 failure_rate = count / length
# 3. 스테이지는 1부터 시작하니 1, N+1 
# 4. 빈 배열에는 (현재 stage, 실패율)을 저장
# 5. 높은 실패율을 기준으로 내림차순 정렬
# 6. 나머지 스테이지 값만 추출해서 배열에 담아서 리턴

# 문제풀이(1)
def solution(N, stages):
    answer = [] # 빈 배열
    length = len(stages) # 스테이지의 길이
    for i in range(1, N+1):
        count = stages.count(i) # N스테이지에서 클리어 못한 사람의 수
        print(stages.count(i))
        if count == 0: # N스테이지에서 클리어 못한 사람의 수가 0과 같다면 0으로 정의
            failure_rate = 0
        else: # 아니라면 실패율 정의
            failure_rate = count / length
            print(failure_rate)
        length -= count # N스테이지에서 클리어 못한 사람만큼 빼기
        print(length)
        answer.append((i, failure_rate)) # 현재 스테이지, 실패율을 빈 배열에 담아놓는다.

    # 실패율이 높은 스테이지부터 내림차순으로 정렬
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))

# 다른사람의 풀이(1)
def solution(N, stages):
    result = {} # 객체 선언
    denominator = len(stages) # N스테이지에 통과한 사람의 수 또는 길이
    for stage in range(1, N+1):
        if denominator != 0: # 통과한 사람의 수가 0이 아닐 때
            count = stages.count(stage) # 스테이지의 수를 count, 1 stage, 2stage ...
            result[stage] = count / denominator # result의 객체에 stage를 담음, {key(count): value(denominator)}
            denominator -= count # 스테이지를 클리어하지 못한 사람(1) - 통과한 사람(8)
        else:
            result[stage] = 0 # 클리어 할 사람이 없을 경우 0으로 정의
    return sorted(result, key=lambda x : result[x], reverse=True)
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))