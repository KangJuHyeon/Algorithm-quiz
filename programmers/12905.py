# 문제접근
# 제일 큰 사각형을 구하고 정사각형의 넓이를 구하는 문제?
# 2중 포문?

# 수도코드
def solution(board):
    answer = 1234
    for i in range(len(board)):
        # print(i)
        for j in range(1, len(board[0])+1):
            # print(j)
            print(board[i][j])

    return answer
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) # 9

# 문제풀이(1)
def solution(board):
    dp = board
    for i in range(1, len(board)): # low [[1],[2],[3],[4]]
        print(i)
        for j in range(1, len(board[0])): # col [[1,2,3,4]]
            print(board[0])
            print(j)
            if board[i][j] != 0: # 0이 아니라면
                dp[i][j] += min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) # dp에 정사각형의 한변의 길이를 저장한다.
                print(dp[i][j]) # 정사각형의 한변의 길이를 dp[i][j]에 저장한다.
    
    answer = max([n for row in board for n in row]) # list comphrehension을 사용한 이중 for문도 기억해두면 좋을 것 같다. => 가장 큰 변의 길이 구하기
    return answer ** 2
            
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) # 9
print(solution([[0,0,1,1],[1,1,1,1]])) # 4


# 다른사람의 풀이(옛날 풀이)
def solution(board):
    ss = {}
    answer = 0
    for y, line in enumerate(board):
        for x, v in enumerate(line):
            if v == 'X':
                continue
            ss[(x,y)] = s = min(
                ss.get((x-1,y), 0),
                ss.get((x,y-1), 0),
                ss.get((x-1,y-1), 0)
            ) + 1
            answer = max(answer, s ** 2)
    return answer
print(solution([['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']])) # 9

# 다른사람의 풀이(2)
def solution(board):
    if len(board) == 1 and len(board[0]) == 1:
        if board[0][0] == 0:
            return 0
        elif board[0][0] == 1:
            return 1
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1],board[i-1][j],board[i][j-1]) +1

    answer = 0
    for i in range(1,len(board)):
        temp = max(board[i])
        answer = max(answer,temp)

    return answer**2
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) # 9