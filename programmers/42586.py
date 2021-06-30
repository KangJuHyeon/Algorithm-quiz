# queue FIFO 을 활용한 풀이
def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0

    while len(progresses) != 0:
        if progresses[0] + days * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        elif count > 0:
            answer.append(count)
            count = 0
        days += 1
        
        answer.append(count)
    return answer

# progresses(작업 진도), speeds(작업 속도), return 값(배포될 때 기능이 완료된 것들)
# progresses(작업 진도)가 0이 아니라면 while문에 들어가고
# 만약 progresses(작업 진도) 리스트 0번 째 인덱스 + days + speeds(작업 속도) 리스트 0번 쨰 인덱스가 100 이하 또는 같다면
# progresses(작업 진도) 리스트 0번 째 인덱스를 빼준다. speeds(작업 속도) 리스트 0번 째도 빼준다. 그리고 count + 1 해줘서 할당시켜준다.
# elif count > 0: (count가 0보다 클때) answer 빈 배열에 count의 값을 추가시켜준다. 그리고 다시 count를 0으로 초기화하고 
# days += 1 작업이 끝났으니 배포일 수를 추가시켜준다.

# 두 번쨰 풀이(stack) LIFO
import math

def solution(progresses, speeds):
    answer = []
    stack = []
    days = 0
    
    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i]) / speeds[i])
        
        if i == 0:
            stack.append(days)
        else:
            if stack[0] >= days:
                stack.append(days)
            else:
                answer.append(len(stack))
                stack.clear()
                stack.append(days)
                
    answer.append(len(stack))
        
    return answer

# 앞에 작업보다 뒷작업이 먼저 끝나면 앞에 작업이 끝날때 까지 기다려야 하므로 각 progresses 마다 배포일을 구한다음,  
# progress 순서대로 배포일을 스택에 담았을때 
# 다음 배포일이 스택에 있는 배포일보다 작다면 스택에 쌓고 다음 배포일이 스택에 있는 배포일보다 크다면, 
# 스택에 있는 것(길이)을 모두 pop 한다음 배포일을 스택에 넣는다.
# 프로그래머스에선 math 함수를 사용해야 통과가 된다.