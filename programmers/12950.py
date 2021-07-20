# 처음 문제 풀이 방법 및 생각
# 이중 포문을 이용해서 행과 열을 더한다.
# 처음 문제 풀이(1)
def solution(arr1, arr2):
    result = []
    for i in range(arr2):
        for j in range(arr1):
            result = i + j
    return list(result)
# TypeError: 'list' object cannot be interpreted as an integer

# 두 번째 풀이(2)
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        result = []
        for j in range(len(arr2[i])):
            result.append(arr1[i][j] + arr2[i][j])
            
        answer.append(result)

# Best 풀이
    return [[x + y for x, y in zip(a, b)] for a, b in zip(arr1, arr2)]

# 이중 포문으로 푸는 방법은 맞았지만 2차원 배열의 대한 개념이 조금 부족했던 것 같다.
# zip 함수로 푸는 방법도 생각해서 풀이도 했었지만 잘 풀리지 않았다.
# 그래서 zip 함수에 대한 공부를 할 수 있게 되어서 좋았고, 1차배열, 2차배열일 때에 코드를 볼 수 있어서 좋았다.
