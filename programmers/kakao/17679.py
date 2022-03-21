# 문제 해결 방법
# 공책으로 적으면서 방법을 찾는 것이 Best 간단하게 적어본다.
# 🗒 1. 행과 열로 만들어서 눈으로 보기 쉽게 블록으로 나눠본다.
# 🗒 2. 제한사항인 2x2 블록들이 만나면 표시를 해줘야한다, 그것을 빈 리스트 6개를 만들어서 0대신 1로 파괴된 블록을 표시한다.
# 🤷 while문을 사용하여, 조건문을 달아주는 형식으로 만들어줘야할 듯 싶다. 2차원 배열이 무엇이라면 j+1이 같은 것이라면 등등
# 🗒 3. zero_one_world에 1로 표시된 블록의 개수를 doll에 저장(doll: 한 텀에 지워진 블록의 개수)
# 🗒 4. 지워진 블록의 개수를 answer에 더함
# 🗒 5. 지워진 블록이 없을 경우 while문을 빠져나옴
# 결국 내 머리로는 지운 블록을 아래로 이동하는 코드 등이 너무 어려웠다. 나중에 다시 풀어보자.

def solution(m, n, board):
    answer = 0
    for i in range(len(board)): 
        board[i] = list(board[i])
        print(board[i])
    
    # 같은 모양 2x2 블록을 찾았을 때 0과 1의 세계의 맛을 보여줌
    while True:
        zero_one_world = [[0] * n for i in range(m)]
        print(zero_one_world)
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][j + 1]:
                    zero_one_world[i][j], zero_one_world[i][j + 1], zero_one_world[i + 1][j], zero_one_world[i + 1][j + 1] = 1, 1, 1, 1
                    print(zero_one_world)
        # 지워진 블록 개수 세기
        doll = 0
        for i in range(m): doll += sum(zero_one_world[i])
        print(doll)
        answer += doll
        # 지워진 블록이 없을 경우 break
        if doll == 0: break
        
        # 지워진 블록을 위의 블록으로 채우기
        for i in range(m - 1, -1, -1):
            for j in range(n):
                print(zero_one_world)
                if zero_one_world[i][j] == 1:
                    a = i - 1
                    print(a)
                    while a >= 0 and zero_one_world[a][j] == 1: a -= 1
                    if a < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[a][j]
                        zero_one_world[a][j] = 1
    return answer
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))