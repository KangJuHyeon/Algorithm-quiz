# 문제 접근
# 2번째부터 5번째 slicing [5,2,6,3] => sort() => [2,3,5,6]
# 위에 과정 [2,3,5,6]의 len(arr)의 3번째 숫자를 추출 => 5
# 입력 값이 2차원 배열이라면? for를 이용해 1차원 배열의 원소를 구한다.
# 헷갈리는데 i = 2, j = 5, k = 3 ??? command 배열의 [2,5,3], [4,4,1], [1,7,3]이 i,j,k 값이었다;
# 그렇다면 i번째부터 시작해서 j번째까지 배열을 자르고, k번째 수를 구해서 새로운 빈 배열에 담아서 리턴하라. 이것이 문제이다.

# 1. 파이썬 슬라이싱(slicing) 기능을 이용해 i부터 j까지 배열 자르기
# 2. 정렬(sort) 기능 이용해 정렬
# 3. 정렬된 리스트에서 k번째 리턴 

# 수도코드
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3],[4, 4, 1],[1, 7, 3]]

answer = []
for i in range(len(commands)):
    print(array[commands[i][0] - 1:commands[i][1]]) # i부터 j까지의 배열을 자른다.
    result = array[commands[i][0]- 1:commands[i][1]]
    result.sort()
    print(result) # 정렬한 배열
    answer.append(result[commands[i][2]-1]) # answer 리스트에 k-1번째 배열 추가 => 3번째 수인 k번 째수를 구해 배열에 push한다.
    print(result[commands[i][2]-1])
print(answer) # 새로운 빈 배열에 k 번째 수를 구해서 담았다.

# 문제풀이(1)
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        result = array[commands[i][0] - 1:commands[i][1]]
        result.sort()
        answer.append(result[commands[i][2]-1])
    return answer

# 다른사람의 BEST 문제풀이(1)
# map 함수와 lambda 함수를 이용해 한 줄로 표현했다.
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))