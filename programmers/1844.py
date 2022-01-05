# 문제 읽기
# 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 리턴하라.
# 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 리턴하라.

# 문제접근
# '최단거리'라는 단어가 나왔기 때문에 BFS/DFS 알고리즘을 생각하게 된다. 혹은 행렬 문제로 보기도 했다.
# 벽이 없는 자리는 1로 표현하고, 벽이라면, 0으로 표현되었다.
# BFS 알고리즘은 매 순간이 최적의 경우(해)임을 보장하기 때문에 '최단거리' 문제에 적용된다.
# BFS 최단거리 알고리즘 구현에 대해서 알아보자.

# 문제에 대한 공부, 이해하기
# deque를 사용한 이유? popleft 사용을 위해 deque 사용했다.
# solution 함수 n, m에 (0,0)을 넣는 이유는 시작 지점의 좌표가 0,0이기 때문이다.

# 문제풀이(1)
from collections import deque

def bfs(maps, n, m):
    queue = deque()
    nm = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우, n, m에서 각 좌표에 따라 더하고 빼주기
    visited = [[0] * len(maps[0]) for i in range(len(maps))] # visited는 지나온 거리마다 1씩 더해서, 몇 칸 만큼 왔는지 체크하기 위한 리스트
    print(visited)
    
    queue.append((n, m))
    visited[n][m] = 1 # 처음 시작 지점은 한 칸을 포함 하므로 1을 넣어준다.
    
    # queue안에 요소가 없으면 while문이 멈춘다.
    while queue:
        n, m = queue.popleft()
        print(n, m)
        # 만약 n,m 좌표가 범위를 넘었을 때, break로 멈춰줘라.
        if n == len(maps) and m == len(maps[0]):
            break

        for i in range(len(nm)):
            dn = n + nm[i][0] # 현재 좌표에서 위, 아래, 왼쪽, 오른쪽으로 갔을 때 좌표
            dm = m + nm[i][1] # 현재 좌표에서 위, 아래, 왼쪽, 오른쪽으로 갔을 때 좌표
            
            # 만약 dn, dm이 0보다 크고, 범위에서 벗어나지 않을 때만, visited좌표에서 한 칸씩 갈 때마다 1씩 더해줌
            if (dn >= 0) and (dm >= 0) and (dn < len(maps)) and (dm < len(maps[0])):
                # maps에서 maps[n][m]가 1이며, visited에서는 0인곳으로만 한칸 전진 가능하다.
                if (maps[n][m] == 1 and visited[dn][dm] == 0):
                    queue.append((dn, dm))
                    print(queue)
                    visited[dn][dm] = visited[n][m] + 1 # 한 칸씩 전진할 때마다 더해주면, 도착지점에 도달 했을 때 모든 칸을 더한 최소값을 반환
                    print(visited[dn][dm])

    return visited[len(maps) - 1][len(maps[0]) - 1]

def solution(maps):
    # 상대 팀 진영에 도착할 수 없을 때
    if not bfs(maps, 0, 0):
        return -1
    # 아니고 상대 팀 진영에 도착할 수 있을 때
    return bfs(maps, 0, 0)
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11 상대 팀 진영에 도착하기 위해 지나가야 하는 최솟값
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1, 상대 팀 진영에 도착할 수 없을 때