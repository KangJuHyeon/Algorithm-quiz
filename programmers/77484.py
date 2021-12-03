# 문제접근
# 0은 알아볼 수 없는 번호이고, 0이 당첨번호와 같을 수도 있다.
# 그러니 최고 순위번호일 경우, 최저 순위 번호일 경우를 빈 배열에 담으면 된다.
# 최고 순위일때, 최저순위일 때를 따로 구해야하나? 로또 순위를 정하는 로직은 여러가지가 나올듯 싶다.

# 에러해결
# 테스트케이스 2번에서 list index out of range => 배열을 6까지 늘려주니 해결되었다.
# 문제는 zero_cnt가 0이 6개가 되는 곳이 있다보니 났었음

# 수도코드(1)
def solution(lottos, win_nums):
    answer = []
    cnt = 0 # 당첨 내용을 카운팅
    
    # 최고 순위일 때
    for i in lottos:
        print(i)
        # 만약 0이 알 수 없는 번호이지만 맞았을 경우와 틀렸을 경우를 판단
        if i in win_nums: # 만약 로또 당첨번호 배열 중 i가 포함되어 있다면
            cnt += 1
        elif i == 0:
            cnt += 1

    # 로또 순위를 정해주는 로직
    if cnt == 6: 
        answer.append(1)
    elif cnt == 5:
        answer.append(2)
    elif cnt == 4:
        answer.append(3)
    elif cnt == 3:
        answer.append(4)
    elif cnt == 2:
        answer.append(5)
    else:
        answer.append(6)

    # 최저 순위일 때
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1

    # 로또 순위를 정하는 로직
    # 당첨 내용이 6개일 때 1등
    if cnt == 6: 
        answer.append(1)
    elif cnt == 5:
        answer.append(2)
    elif cnt == 4:
        answer.append(3)
    elif cnt == 3:
        answer.append(4)
    elif cnt == 2:
        answer.append(5)
    else:
        answer.append(6)
            
    return answer
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

# 문제풀이(1)
def solution(lottos, win_nums):
    ranking = [6, 6, 5, 4, 3, 2, 1] # 순위를 선언
    cnt = 0 # 로또 당첨번호와 맞는 숫자를 카운팅
    zero_cnt = 0 # 0을 카운팅하는 숫자(0이 맞는 숫자인지, 아닌지 판별)

    # 0이 맞을 때
    for i in lottos:
        if i == 0:
            zero_cnt += 1
    
    # 0이 아닐 때
    for i in lottos:
        if i in win_nums:
            cnt += 1
    
    # 0이 맞는숫자이고 최고 순위일 때
    max_ranking = ranking[zero_cnt + cnt]
    # 0이 맞지않고 최저 순위일 때
    min_ranking = ranking[cnt]

    return [max_ranking, min_ranking]
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))

# 다른사람이 푼 문제(1)
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]