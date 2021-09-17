# 문제 읽기
# 땅따먹기 게임을 하려고 합니다.
# 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다.
# 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다.
# 단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

# 예를 들면,
# | 1 | 2 | 3 | 5 |
# | 5 | 6 | 7 | 8 |
# | 4 | 3 | 2 | 1 |
# 로 땅이 주어졌다면, 1행에서 네번째 칸 (5)를 밟았으면, 2행의 네번째 칸 (8)은 밟을 수 없습니다.

# 마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 리턴하는 함수를 작성하시오.
# 위 예의 경우, 1행의 네번째 칸(5), 2행의 세번째 칸(7), 3행의 첫번째 칸(4) 땅을 밟아 16점이 최고점이 되므로 16을 리턴하면 된다.

# land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]], answer = 16

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

# 문제풀이(1)
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