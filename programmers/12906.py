# 문제풀이(1) 중복제거
def solution(arr):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    return answer

# 문제풀이(2) 문제의도를 파악하여 다시풀기
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if(i == 0):
            answer.append(arr[i])
        elif(arr[i] != arr[i-1]):
            answer.append(arr[i])
    return answer

# 처음 문제 풀이
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고, 남은 수를 리턴하라.
# 집합 자료형을 이용하여 중복제거(set)
# for문을 이용하여 중복제거하기

# 위에처럼 중복제거를 해보았지만, 한가지 통과가 안됐다. 문제의도를 다시 생각해보았다.
# 문제의도는 중복제거가 아닌, 연속적인 값이 들어가면 안되고, 
# 빈 배열 안에 값이 없다면 넣고, 그 값이 같지 않다면 값을 넣는다.
# [1, 1, 3, 3, 0, 1, 1] => [1, 3, 0, 1] 
# 3의 값이 1과 같은가? 0의 값이 3과 같은가? 아니면 넣고, 같다면 제거한다.