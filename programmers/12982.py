# 문제접근
# 부서가 담긴 d와 얼마를 지원할 수 있는지 담긴 budget를 비교하면 된다.
# budget이 i를 뺼수없다면 멈추고, 아니라면 카운팅을 진행하면서 계속 뺸다.

def solution(d, budget):
    answer = 0 # 몇 개의 부서에 물품을 지원할 수 있는지 카운팅
    for i in sorted(d):
        if budget < i:
            break
        else:
            answer += 1
        budget -= i

    return answer
print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))

# 다른사람의 풀이(1)
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

