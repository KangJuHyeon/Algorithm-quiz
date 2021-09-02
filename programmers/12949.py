# 문제 읽기
# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수를 만들어라.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
# 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
# 곱할 수 있는 배열만 주어집니다.

# arr1 = [[1,4],[3,2],[4,1]], arr2 = [[3,3],[3,3]]

# 문제 접근
# 둘다 2차원 배열이니까 arr1을 i 값으로 추출하고, arr2도 j로 추출해서
# arr1[i] * arr2[j] 이런식으로 값을 곱하고 2차원 배열에 넣어주면 될 것 같다.
# 추출해도 더하기에서 막히고 배열의 2개의 원소를 어떻게 넣을지도 고민이 생겼다.
# 행렬의 곱셈 수학 강의를 듣고, 접근 방식에 대한 방법을 알았다.
# 행렬의 방식을 사용하는 것이 컴퓨터이기 떄문에 꼭 알아둬야하는 수학 공식이라고 들었던 것 같다.
# 행렬의 곱셉을 구할 떈 삼중 포문을 사용한다.

# 수도코드(1)
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        newArr = []
        # print(i)
        for j in range(len(arr2[0])):
            newArr = arr1[i][j] * arr2[j][1] # 3,12,9,6,12,3 더하기? 어떻게 만들지? [[3,12],[9,6],[12,3]]
            print(newArr)
    # answer.append(newArr)
    # print(answer)
print(solution([[1, 4], [3, 2],[4, 1]], [[3, 3], [3, 3]]))


# 문제풀이(1)
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)): 
        newArr = []
        # print(i)
        for j in range(len(arr2[0])): 
            cnt = 0
            for k in range(len(arr2)):
                cnt += arr1[i][k] * arr2[k][j]
                print(cnt)
            newArr.append(cnt)
        answer.append(newArr)
    print(answer)
print(solution([[1, 4], [3, 2],[4, 1]], [[3, 3], [3, 3]]))