# 문제 접근
# 배열을 나누어? [] % divisor = [5, 10] ?
# 배열을 정렬해서 답을 추출해야 할 듯? [2, 3, 36] ???
# [5, 9, 7, 10], 5
# [2, 36, 1, 3], 1
# [3, 2, 6], 10
# 수도코드
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor:
            answer += i
        else:
            return [-1]

# 문제풀이(1)
def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0: # 0이 안들어가면 답이 안나옴 나누어 떨어져야되기 때문이다.
            answer.append(arr[i])
    if len(answer) == 0: # 만약 answer 배열이 비어 있다면 -1을 리턴하고,
        answer.append(-1)
    else:                # 아니라면 answer을 정렬해서 리턴한다.
        answer.sort()
    return answer