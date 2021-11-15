# 문제접근
# signs의 값이 false이면 absolutes의 값이 음수, true일 경우 absolutes의 값이 양수

# 문제풀이(1)
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        print(signs[i])
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
print(solution([4, 7, 12],[True, False, True])) # 9
# print(solution([1, 2, 3],[False, False, True])) # 0

# 다른사람의 문제풀이(1)
def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer