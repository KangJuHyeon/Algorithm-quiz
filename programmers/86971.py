# 문제접근
# 최선의 방법을 구하는 것이기 때문에 BFS 알고리즘을 사용해야된다고 생각했다.
# 전선을 하나씩 끊어보고, 한 쪽만 BFS로 탐색하며 한 쪽 전력망에 속한 송전탑의 개수를 세어보고 남은 송전탑들과 얼마나 차이나는지 비교하면 된다.

# (1)
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    result = 1
    visited[start] = True 
    while queue:
        v = queue.popleft()
        print(v)
        for i in graph[v]:
            if not visited[i]:
                result += 1
                queue.append(i)
                print(queue)
                visited[i] = True
    return result

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for v1,v2 in wires:
        graph[v1].append(v2)
        print(graph[v1])
        graph[v2].append(v1)
            
    for start,not_visit in wires:
        visitied = [False]*(n+1)
        visitied[not_visit] = True
        result = bfs(graph, start, visitied)
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))
    return answer

# (2)
from collections import deque

def bfs(visited, n, graph):
    queue = deque()
    count = 0
    queue.append(visited)

    v = [0 for _ in range(n+1)]
    v[visited] = 1

    while queue:
        visited = queue.popleft()
        
        for i in graph[visited]:
            if not v[i]:
                v[i] = 1
                queue.append(i)
                count += 1
    return count

def solution(n, wires):
    global answer
    graph = [[] for i in range(n+1)]
    print(graph)

    # 인접 리스트가 만들어지는 과정(이 부분은 신기하다.)
    for i in range(n-1):
        # print(graph[wires[i][0]])
        print(graph[wires[i][0]])
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])
        # print(graph[wires[i][1]])
    
    # 하나씩 연결을 끊고 개수를 확인한다.
    for i in range(n-1):
        graph[wires[i][0]].remove(wires[i][1])
        graph[wires[i][1]].remove(wires[i][0])

        node1 = bfs(wires[i][0], n, graph)
        node2 = bfs(wires[i][1], n, graph)

        answer = min(answer, abs(node1 - node2)) 
        
        graph[wires[i][0]].append(wires[i][1]) 
        graph[wires[i][1]].append(wires[i][0]) 
    
    return answer

answer = float('inf')
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # 3
print(solution(4, [[1,2],[2,3],[3,4]])) # 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])) # 1