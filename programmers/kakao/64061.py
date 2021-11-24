# 문제접근
# 빈 배열을 하나 만들어서 그 배열안에 같은 캐릭터가 2번 만나면 pop, 그것을 카운팅하면 된다.
# board의 값을 어떻게 추출하지? [0, 2, 5, 0, 1]

# 알게 된 내용
# 2차원 배열을 추출할때 길이로 추출하면 board[j][moves[i]-1] 이런식으로 추출한다.
# moves가 길이로 반복문에 안돌아갈 경우, board[j][i-1] 이런식으로 추출이 가능하다.

# 수도코드
def solution(board, moves):
    # 오른쪽 빈 배열 선언 == stack
    stack = []
    # 몇개의 인형이 사라졌는지 카운팅해야된다.
    doll = 0
    # moves 배열을 반복해서 board 값을 추출해야 된다.
    for i in range(len(moves)):
        # board의 1차원 배열의 몇 번째 인덱스인지 확인할 변수를 선언
        idx = 0
        # board의 값을 추출하는 방법 == board[j][i] len?
        for j in range(len(board)):
            # 인형이 없는 곳에서 크레인을 작동시키는 경우 아무일도 일어나지 않는다.
            if board[j][moves[i]-1] == 0:
                continue
            # 인형이 있다면 인형을 가져가고 그 곳은 0으로 표시되어야 한다.
            elif board[j][moves[i]-1] != 0:
                # moves에 맞춰 값을 board에서 stack으로 push
                stack.append(board[j][moves[i]-1])
                # 뽑은 인형은 0으로 표시하는 코드가 있어야 된다. a = 0
                board[j][moves[i]-1] = 0
                # moves의 길이 만큼 더 포문이 돌아가기 때문에 break
                break
    # stack의 길이가 0이 아니거나, stack의 앞 뒤의 값이 같다면
        if stack != 0 and stack[-1] == stack[-2]:
            # 인형을 터트린다. 2번 터트려야된다.
            stack.pop()
            stack.pop()
            # 터트린 인형을 카운트한다.
            doll += 2;
            # 터트린 인형 갯수를 리턴
        return doll
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

# 문제 풀이(1)
def solution(board, moves):
    stack = []
    doll = 0 
    for i in moves:
        for j in range(len(board)):
            # print(board[j][i-1]) # board의 값을 추출함
            if board[j][i-1] == 0:
                continue
            elif board[j][i-1] != 0: 
                stack.append(board[j][i-1]) 
                board[j][i-1] = 0
                break

        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack = stack[:-2]
            doll += 2

    return doll
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])) # 4