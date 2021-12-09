# 문제 접근
# 2차원 배열의 값을 추출해야한다.
# 추출한 값이 1행과 2행을 비교하여 인덱스의 값이 중복된다면 땅을 밟을 수 없다.
# 1행 [0, 1, 2, 3], 2행 [0, 1, 2, 3] 기준 같은 3번은 안된다.

# 수도코드(1)
def solution(land):
    answer = [] # 1열의 값을 넣을 상자
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            # print(land[i][j])
            Earth = land[i][j]
            print(Earth)
print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))

# 수도코드(2)
# 정확성 0%, 효율성 0%
def solution(land):
    answer = 0 
    num = 4 # 첫 행에서는 num이 영향을 미치면 안되므로 열의 총 수인 4를 대입했다.
    for i in range(0, len(land)): # 0번째 행부터 len(land)-1행까지 반복
        cnt = 0
        print(i)
        for j in range(0, 4): # 각 행의 열들을 반복
            if num == j: # 바로 직전의 행과 같은 열을 밟을 수 없다.
                continue
            if land[i][j] > land[i][cnt]:
                print(land[i][j])
                print(cnt)
                cnt = j # 각 열에서 최대값을 더해주기
                print(cnt)
        answer += land[i][cnt] # 최대값들 더해주기
        print(answer)
        num = cnt # 이번 행에서 최대였던 열을 저장하여 다음 행에 영향을 준다.
        print(num)
    return answer
print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))

# dp 문제 풀이(1)
def solution(land):
    answer = 0
    for i in range(0, len(land)-1):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    return max(land[-1])
print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))

# 문제풀이(2)
def solution(land):
    ans = [[land[0][0], land[0][1], land[0][2], land[0][3]]]
    for i in range(1, len(land)):
        ans.append([0, 0, 0, 0])
        ans[-1][0] = land[i][0] + max(ans[i-1][1], ans[i-1][2], ans[i-1][3])
        ans[-1][1] = land[i][1] + max(ans[i-1][0], ans[i-1][2], ans[i-1][3])
        ans[-1][2] = land[i][2] + max(ans[i-1][1], ans[i-1][0], ans[i-1][3])
        ans[-1][3] = land[i][3] + max(ans[i-1][1], ans[i-1][2], ans[i-1][0])

    return max(ans[-1][0], ans[-1][1], ans[-1][2], ans[-1][3])