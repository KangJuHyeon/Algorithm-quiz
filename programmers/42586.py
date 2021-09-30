# queue FIFO 을 활용한 풀이
def solution(progresses, speeds):
    answer = [] # 기능 배포한 갯수를 담을 상자
    days = 0  # 걸린 날짜
    count = 0 # 기능을 배포한 갯수

    while len(progresses) != 0: # 진행상황이 0이 아니라면
        if (progresses[0] + days * speeds[0]) >= 100: # 100이 넘어가면 완료된 것이니까 더 크거나 같다면 조건문을 주었다.
            progresses.pop(0)
            # print(progresses)
            speeds.pop(0)
            # print(speeds)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                print(answer)
                count = 0
            days += 1

    answer.append(count)

    return answer
print(solution([93, 30, 55], [1, 30, 5]))
# progresses(작업 진도), speeds(작업 속도), return 값(배포될 때 기능이 완료된 것들)
# progresses(작업 진도)가 0이 아니라면 while문에 들어가고
# 만약 progresses(작업 진도) 리스트 0번 째 인덱스 + days + speeds(작업 속도) 리스트 0번 쨰 인덱스가 100 이하 또는 같다면
# progresses(작업 진도) 리스트 0번 째 인덱스를 빼준다. speeds(작업 속도) 리스트 0번 째도 빼준다. 그리고 count + 1 해줘서 할당시켜준다.
# elif count > 0: (count가 0보다 클때) answer 빈 배열에 count의 값을 추가시켜준다. 그리고 다시 count를 0으로 초기화하고 
# days += 1 작업이 끝났으니 배포일 수를 추가시켜준다.

# 두 번쨰 풀이(stack) LIFO
import math

def solution(progresses, speeds):
    answer = [] # 몇개의 기능을 담을 상자
    stack = []  # 기능에 걸린 날짜
    days = 0    # 일수 카운트
    
    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i]) / speeds[i])

        if i == 0:
            stack.append(days)
            # print(stack)
        else:
            if stack[0] >= days:
                stack.append(days)
                # print(stack)
            else: # 배포일이 stack에 있는 배포일보다 클 경우 stack pop
                answer.append(len(stack))
                # print(answer)
                stack.clear()
                # print(stack)
                stack.append(days)
                # print(stack)
                
    answer.append(len(stack))
        
    return answer
print(solution([93, 30, 55], [1, 30, 5]))
# 앞에 작업보다 뒷작업이 먼저 끝나면 앞에 작업이 끝날때 까지 기다려야 하므로 각 progresses 마다 배포일을 구한다음,  
# progress 순서대로 배포일을 스택에 담았을때 
# 다음 배포일이 스택에 있는 배포일보다 작다면 스택에 쌓고 다음 배포일이 스택에 있는 배포일보다 크다면, 
# 스택에 있는 것(길이)을 모두 pop 한다음 배포일을 스택에 넣는다.
# 프로그래머스에선 math 함수를 사용해야 통과가 된다.