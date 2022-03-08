# NOTE 문제접근
# 최단 경로 알고리즘?과 비슷하지만 BFS로 구현할 예정
# 옆에 있는 노드의 시간을 더했을 때, K이하의 값이어야한다. 아니라면 다른 노드를 순회
# 5개의 마을을 먼저 만들고, 2차원 배열을 조건을 통해 큐에 담고, pop을 하면서 배달할 수 있는 마을을 구한다.
# 마을을 담을 필요없이 road의 K값을 받아오는 것이 더 중요하다. 마을 필요 x
# 다익스트라 알고리즘?을 사용해도 풀릴 것 같다. 객체로 간선 정보들을 입력해도 될 것 같다.

# TODO
# 동빈나 동영상을 보고 접근은 했는데, 내 코드가 다익스트라 알고리즘과 비슷한 것 같은데 정확하게 알 수가 없다.
# 아래 다른 코드들과 함께 깨달아야할 것 같다.

# 수도코드(1)
import math
from collections import deque

def bfs(start, towns, distance, K):
    queue = deque()
    queue.append(start)
    print(queue)

#     # 방문한 노드들을 체크
#     # visited = [[0] * len(towns) for i in range(len(towns))]
#     # print(visited)

#     # 처음 출발한 도시의 거리는 0으로 지정
    distance[start] = 0
    # print(distance[start])
    while queue:
        temp = queue.popleft()
        for i in range(1, len(towns)):
#             # 도착할 수 있는 도시인 경우
            if towns[temp][i] != 0:
                # 해당 마을까지의 거리가 현재까지의 거리 + 이동할 때 걸리는 거리보다 작다면 배달 가능 지역이다.
                # 현재까지의 거리 + 이동할 때의 거리가 K보다 작다면? ex) K = 3, 3보다 작다면 배달 가능한 지역
                if distance[i] > distance[temp] + towns[temp][i] and distance[temp] + towns[temp][i] <= K:
                    distance[i] = distance[temp] + towns[temp][i]
                    # print(distance[i])
                    queue.append(i)
                    # print(queue)
    # distance 값 중 K보다 작은 값의 개수만 리턴한다.
    # 이게 어떻게 한줄만 되는건지 모름
    # return distance[i] + 1
    return len([i for i in distance if i <= K])

def solution(N, road, K):
    answer = 0
    # 시작지점 1에서부터 해당 마을까지의 거리를 구해야한다.
    # 초기값을 어떻게 정함? inf로 설정하고, 계산한 거리가 distance[마을]보다 작으면 distance를 업데이트해준다.
    # 근처에 있는 배달 지역은 거리로 표시하고, 지금 내 위치에서 갈 수 없는 지역은 무한으로 지정한다.
    distance = [math.inf for _ in range(N+1)]
    print(distance)
    
    # 마을의 간선, 거리를 배열에 담아보자
    # 거리를 구해야되기 때문에 간선을 배열로 보여주는게 맞다고 생각, 마을은 x 필요없음
    Towns = [[0 for _ in range(N+1)] for _ in range(N+1)]
    # print(Towns)

    # N번 마을에서 K시간 이상인 배달을 갈 수 없는 마을 갯수
    for one, two, three in road:
        # 0이라면 초기화한 값 그대로이므로 three값을 넣어준다.
        if Towns[one][two] == 0 and Towns[two][one] == 0:
            Towns[one][two], Towns[two][one] = three, three
            print(Towns[one][two], Towns[two][one])
        else:
            # 중복된 값이 있을 경우, 가장 작은 값만 사용한다.
            if three < Towns[one][two]:
                Towns[one][two], Towns[two][one] = three, three
                print(Towns[one][two], Towns[two][one])

    # if not bfs(Towns, distance, N, K): 
        # return -1
    # N번 마을에서 K시간 이하인 마을들 갯수
    # return bfs(1, distance, Towns, K)

    return bfs(1, Towns, distance, K)
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
# print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))


# 문제 해결 방법
# 1. 간선의 정보를 탐색
# 2. 양방향 간선이기 때문에 양쪽의 노드에 간선 정보를 함께 저장
# 3. 각 노드별 가장 큰 수를 저장할 dict인 distance를 생성
# 4. 시작점을 기준으로 BFS
# 5. 출발점과 노드의 거리를 가장 짧은 값으로 갱신해주며 진행
# 6. distance의 key, value를 확인하여 value가 K보다 작은 노드의 개수를 출력
# 📌 대부분의dijkstra문제는 heap을 사용하지만, 이 문제는 노드와 간선의 개수가 작아 굳이 heap을 사용할 필요 X

# 다른사람의 풀이(1)
from collections import deque

def solution(N, road, K):
    answer = 0

    nodes = {}
    for v1, v2, dis in road:
        nodes[v1] = nodes.get(v1, []) + [(v2, dis)]
        nodes[v2] = nodes.get(v2, []) + [(v1, dis)]

    distance = {i:float('inf') if i != 1 else 0 for i in range(1, N + 1)}

    # 1번 노드와의 거리 저장
    deq = deque([1])
    while deq:
        current_node = deq.popleft()
        for next_node, dis in nodes[current_node]:
            if distance[next_node] > distance[current_node] + dis:
                distance[next_node] = distance[current_node] + dis
                deq.append(next_node)

    answer = len([True for val in distance.values() if val <= K])

    return answer