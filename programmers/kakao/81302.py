# 1. 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
# 2. 거리두기를 위하여 응시자들 끼리는 맨해튼 거리가 2 이하로 앉지 말아 주세요.
# 3. 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

# 5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리두기를 잘 지키고 있는지 알고 싶어졌습니다.
# 자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실 별로 담은 2차원 문자열 배열 places가 매개변수로 주어집니다.
# 각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 리턴하도록 함수를 완성해주세요.

# P는 응시자가 앉아있는 자리를 의미한다.
# O는 빈 테이블을 의미한다.
# X는 파티션을 의미한다.

# 상하좌우를 표현해야 한다.
# P에서 X를 만나면 정지
# P가 O를 만나면 빈 테이블이므로 쭉 진행
# 2보다 작으면 거리두기 실패, 하지만 2와 같거나 크다면 거리두기 성공

def solution(places):
    answer = []
    for place in places:
        judgment = False # 거리두기 했는지 안했는지
        violators = [] # 위반자들
        
        # 하나씩 담아서 대기실을 구현
        for div in place:
            # 슬라이싱 말고 다른 방법
            # distanceTable = list(div[::-1]) 
            violators.append(list(div))
        print(violators)

        # 이중 for문을 돌아서 옆, 아래를 순회한다.
        for i in range(5):
            if judgment:
                break
            
            # 이중 for문을 돌아서 옆, 아래를 순회한다.
            for j in range(5):
                if judgment:
                    break

                # print(violators[i][j]) # 결과가 잘나오는지 확인
                
                # 만약 지금 위치가 사람이라면
                if violators[i][j] == "P":
                    # 제일 긴 숫자 5보다 작을 때
                    if i + 1 < 5:
                        # 옆 + 1 옆을 확인한다, 근데 사람이라면?
                        if violators[i+1][j] == "P":
                            judgment = True
                            break

                        if violators[i+1][j] == "O":
                            if i + 2 < 5:
                                if violators[i + 2][j] == "P":
                                    judgment = True
                                    break
                    if j + 1 < 5:
                        if violators[i][j+1] == "P":
                            judgment = True
                            break
            
        if (div[4]):
            print("--------------------방화벽--------------------")
    return answer
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# 문제풀이(2)
from collections import deque

def bfs(p):
    start = []

    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
                print(start)
    
    for i in start:
        queue = deque([i]) # 큐에 초기값
        visited = [[0] * 5 for i in range(5)] # 방문 처리 리스트
        distance = [[0] * 5 for i in range(5)] # 경로 길이 리스트
        visited[i[0]][i[1]] = 1
        
        while queue:
            y, x = queue.popleft()

            distanceX = [-1, 1, 0, 0] # 좌우
            distanceY = [0, 0, -1, 1] # 상하
            
            for i in range(4):
                nx = x + distanceX[i]
                ny = y + distanceY[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                    
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))