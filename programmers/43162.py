# 문제풀이(1) - DFS
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    # print(visited)
    for compute in range(n):
        if visited[compute] == False:
            dfs(n, computers, compute, visited)
            answer += 1 # dfs로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크
    return answer
                
def dfs(n, computers, compute, visited):
    print("n은 {}, computers는{}, compute는 {}, visited는 {}".format(n, computers, compute, visited))
    visited[compute] = True
    for i in range(n):
        print("i", i)
        print("2차원 배열 값 구하기", computers[compute][i])
        if i != compute and computers[compute][i] == 1: # 연결된 컴퓨터
            if visited[i] == False:
                dfs(n, computers, i, visited)

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # return 2
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # return 1

# 문제풀이(2) - BFS
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1
    return answer

def BFS(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # return 2
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # return 1

# 문제풀이(3) - index
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    box = []

    while all(visited) != True:
        box.append(visited.index(False))
        print(box)
        while box:
            node = box.pop()
            print(node)
            visited[node] = True
            for i in range(len(computers[node])):
                if i != node and computers[node][i] == 1 and visited[i] != True:
                    visited[i] = True
                    box.append(i)
        answer += 1
    
    return answer
print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # return 2
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # return 1