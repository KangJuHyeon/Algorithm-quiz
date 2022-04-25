# 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받는다.
# 게임 찾가자 수 N
# 참가자 번호 A
# 경쟁자 번호 B
# 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return 하는 solution 함수를 완성해 주세요

# 대진표를 노트에 적어보고, 규칙을 찾아야한다.
# 1라운드에는 4번은 -> 2번으로, 7번은 -> 4번으로 변환
# 2라운드에는 2번이 -> 1번으로, 4번은 -> 2번으로 변환
# 3라운드에는 만나야하는 1번과 2번이 3라운드에 만났으므로, answer = 3
# a, b가 같은 번호가 되었을 때, 승리를 3번했다는 카운팅

# 문제풀이(1)
def solution(n,a,b):
    answer = 0
    
    while a != b:
        if a % 2 == 1:
            a = (a + 1) / 2
            print(a)
        else:
            a = a / 2
            print(a)

        if b % 2 == 1:
            b = (b + 1) / 2
            print(b)
        else:
            b = b / 2
            print(b)
        print(a, b)
        answer += 1

    return answer
print(solution(8, 4, 7)) # 3

# 다른사람의 풀이(1)
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
print(solution(8, 4, 7)) # 3