# 첫 번째 풀이
def solution(priorities, location):
    count = 0
    while len(priorities) != 0:
        if location == 0: # 출력 여부를 확인되는 맨 앞 순서로 왔을 경우
            if priorities[0] < max(priorities): # 더 중요도가 큰 문서가 있다면
                priorities.append(priorities.pop(0)) # 맨 뒤로 보냄
                location = len(priorities) - 1 # location을 맨 끝으로 설정(배열 길이 - 1)
            else: # 더 우선순위가 높은 것이 없다면 내 것이 출력되는 것이므로 return으로 끝냄
                return count + 1
        else:
            if priorities[0] < max(priorities):
                priorities[0] < max(priorities.pop(0))
                location -= 1 # 맨 앞 요소가 뒤로 갔기 때문에 locationdl 1 줄어듬
            else:
                priorities.pop(0) # 맨 앞 요소 출력
                location -= 1 # 맨 앞 요소가 출력되었기 때문에 location 1 줄어듬
                count += 1 #(출력번째수 +1)
                
    return count

# 문제 풀기 전 어떻게 풀어야할지를 메모
# 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 리턴하도록 solution을 만드시오.
# 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼낸다. ["J", "A", "B", "C", "D"] => ["A", "B", "C", "D"]
# 만약 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣는다. 
# if(J가 담긴 배열 < J보다 중요도가 높은 문서) => ["B", "D", "C", "A"] => ["D", "C", "A", "B"]
# 순서를 정렬해서 담을까? sorted(priorities, reverse=True) 

# 두 번째 풀이
def solution(priorities, location):
    answer = 0
    
    # 인쇄 대기목록이 남아있다면 반복
    while len(priorities) != 0:
        # 1. 대기목록의 가장 앞에있는 문서가 나머지 문서들보다 중요도가 높은 경우
        if priorities[0] == max(priorities):
            answer += 1
            priorities.pop(0) # 먼저 인쇄 == 가장 앞에있는 것 삭제
            if location == 0:
                return answer
            else:
                location -= 1
        #2. 대기목록의 가장 앞에있는 문서가 중요도가 가장 높지 않은 경우
        else :
            priorities.append(priorities.pop(0)) #문서를 대기목록 맨 뒤로 이동
            if location == 0:
                location = len(priorities) - 1
            else :
                location -= 1
    return answer

