# 출제의도
# 4방향 이동/회전 구현을 할 수 있는지

# 문제 읽기
# 빛이 "S"가 써진 칸에 도달한 경우, 직진합니다.
# 빛이 "L"이 써진 칸에 도달한 경우, 좌회전을 합니다.
# 빛이 "R"이 써진 칸에 도달한 경우, 우회전을 합니다.
# 빛이 격자의 끝을 넘어갈 경우, 반대쪽 끝으로 다시 돌아옵니다. 
# 예를 들어, 빛이 1행에서 행이 줄어드는 방향으로 이동할 경우, 같은 열의 반대쪽 끝 행으로 다시 돌아옵니다.

# 문제에 대한 회고
# 너무 어려워서 접근조차 못했다. 
# 할 수 있는 것은 BFS/DFS 코드 구현 해놓은 것을 문제랑 비교하면서 맞춰보는 일밖엔...
# 그리고 여기선 빛을 어느 방향에서 쏘는지를 생각해야된다.
# 프로그래머스 블로그에 수도코드에 보면 for문이 3개가 있는 이유는 각 방향에서 오는 경우를 따지는 것이 아닐까 싶다.
# 어쨌든 누군가가 무료로 알려주면 좋겠다. 😱
# 처음으로 단단한 벽에 부딫힌 느낌이든다.

# 풀이(1)
from collections import deque
def solution(grid):
    answer = []
    len_x, len_y = len(grid), len(grid[0])
    visited = [[[0]*4 for _ in range(len_y)] for _ in range(len_x)]
    print(visited)
    direction_dict = {0:(-1, 0), 1:(-1, 0), 2:(0, -1), 3:(0, 1)}
    next_move_dict = {'S':{0:0, 1:1, 2:2, 3:3}, 'L': {0:3, 1:2, 2:0, 3:1}, 'R':{0:2, 1:3, 2:1, 3:0}}
    # print(next_move_dict)
    for i in range(len_x): # 좌우
        for j in range(len_y): # 상하
            while 0 in visited[i][j]:
                queue = deque()
                print(queue)
                # do something
                idx = visited[i][j].index(0)
                print(idx)
                # serach
                queue.append((i,j,idx,1,[i,j,idx]))
                print(queue)
                visited[i][j][idx] = 1 # 해당 경로 방문처리
                print(visited[i][j][idx])
                while queue:
                    x, y, move, counting, first_move = queue.popleft()
                    df_x, df_y = direction_dict[move]
                    print(df_x, df_y)
                    x, y = x + df_x, y + df_y
                    print(x, y)
                    if x == len_x:
                        x = 0
                    elif x < 0:
                        x = len_x-1
                    if y == len_y:
                        y = 0
                    elif y < 0:
                        y = len_y-1
                    next_idx = next_move_dict[grid[x][y]][move]
                    if [x,y,next_idx] == first_move:
                        answer.append(counting)
                    else:
                        visited[x][y][next_idx] = 1
                        queue.append((x,y,next_idx,counting+1,first_move))
    return sorted(answer)
# print(solution(["SL","LR"]))
print(solution(["S"]))
# print(solution(["R","R"]))

# 풀이(2)
import sys
sys.setrecursionlimit(10 ** 6) # 재귀허용 깊이 추가

def out(x, y, d, grid, dic):
    # 방향에 따라 x, y 좌표를 업데이트
    nx = x + dic[d][0]
    ny = y + dic[d][1]
    
    if nx >= len(grid): # 아래쪽으로 넘어갈 때
        nx = 0
    elif nx < 0: # 위쪽으로 넘어갈 때
        nx = len(grid) - 1
    if ny >= len(grid[0]): # 오른쪽으로 넘어갈 때
        ny = 0
    elif ny < 0: # 왼쪽으로 넘어갈 때
        ny = len(grid[0]) - 1
    return nx, ny

def dfs(state, org, route, grid):
    # 방향: 아래쪽에서, 왼쪽에서, 위쪽에서, 오른쪽에서 빛이 들어옴
    dic = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
    x = state[0]
    y = state[1]
    d = state[2]
    visited[d][x][y] = 1
    
    nx, ny = out(x, y, d, grid, dic) # 좌표 업데이트
    value = grid[nx][ny]
    
    # 어느 방향에서 온 것인지를 고려한 계산법
    # ex) 현재 value=R이고, 위쪽 노드에서 온 것(d=2)이라면 우회전 즉 d=3이 되어야 함
    if value == 'R':
        d = (d + 5) % 4
    elif value == 'L':
        d = (d + 7) % 4
    
    # 처음 노드와 비교해서 싸이클일 경우 answer에 싸이클 길이 추가
    if org[0] == nx and org[1] == ny and org[2] == d:
        answer.append(route)
        return
    if not visited[d][nx][ny]: # 방문하지 않는 노드가 있으면 dfs 재귀반복
        dfs([nx, ny, d], org, route + 1, grid)
        
def solution(grid):
    global answer, visited
    answer = []
    # visited = n(행 갯수) x m(열 갯수) x d(방향)
    visited = [[[0] * len(grid[0]) for _ in range(len(grid))] for _ in range(4)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4): # 4가지 방향
                dfs([i, j, d], [i, j, d], 1, grid)
    return sorted(answer)
