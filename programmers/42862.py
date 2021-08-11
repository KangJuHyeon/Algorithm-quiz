# 문제 읽기(지문 파악)
# 체육 수업을 들을 수 있는 학생의 최댓값을 리턴하라. => 얼마나 많은 학생들이 체육복을 입을 수 있느냐.
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어진다.
# reserve 배열에 있는 학생들은 여벌이 존재하기에, 자신의 앞, 뒤 번호 학생들에게 체육복을 빌려줄 수 있다.

# 제한사항
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

# 탐욕법 : 제일 최적의 해를 선택하는 알고리즘
# 나보다 높은 번호를 우선적으로 주는 방법, 나보다 낮은 번호를 우선적으로 주는 방법
# 만약 나보다 높은 번호를 우선적으로 준다면, 문제를 풀 수가 없다.
# 낮은 번호를 우선적으로 준다면 위에 경우 x
# 항상 최적해를 도달하는 방식은 자신보다 낮은 번호부터 주는 것이다.

# 나의 문제 접근
# 도둑은 여벌 옷을 가지고 있는 학생들의 체육복도 하나 훔쳐갈 수 있고, 그럴 경우 그 학생은 빌려줄 수 없다. (왜 훔쳐가 그걸 그니까ㅠㅠㅠ)
# reserve와 lost의 중복되는 값을 제거해야된다.
# 중복 제거후에 둘 중에 하나라도 빈 리스트일 경우 => n - len(n, lost)
# 그 이후 어떻게 풀어야되지 어헝어헝 탐욕뻡이 먼대ㅠㅠㅠㅠ

# 수도코드(1)
def solution(n, lost, reserve):
    result = set(lost) & set(reserve)
    # 만약에 reserve가 result에 포함되어 있다면 reserve 배열을 삭제한다.
    # n - len(n)
    # 중복 제거 후에 어떻게? 풀어야되지 모르겠음...

# 다른사람의 문제풀이(1)
def solution(n, lost, reserve):
    answer = n - len(lost)
    
    for i in lost:
        # 여벌옷 가져온 학생이 도난당했다면
        if i in reserve:
            answer += 1
            reserve.remove(i)
            continue
        
        # 앞 친구에게 먼저 빌리기
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
            continue
            
            
        # 도난당하지 '않은' 뒤 친구에게 빌리기
        if i+1 in reserve and i+1 not in lost:
            answer += 1
            reserve.remove(i+1)
            
    
    return answer

# 다른사람의 풀이(2)
def solution(n, lost, reserve): 
    reser_del = set(reserve)-set(lost) # 체육복 여벌이 있던 학생 중 잃어버린 학생 빼고 = 빌려줄수 있는 학생
    lost_del = set(lost)-set(reserve) # 체육복을 잃어버린 학생 중 여벌이 없는 학생 = 참가불가

    # 참가 가능한 학생 중
    for i in reser_del:
        if i-1 in lost_del: # 왼쪽이 체육복이 없는 경우
            lost_del.remove(i-1) 
        elif i+1 in lost_del: # 오른쪽이 없는 경우
            lost_del.remove(i+1) 
    
    return n-len(lost_del)

# 위에 설명
# 탐욕법 알고리즘을 찾아보며 해답을 얻었다
# 문제에서 lost와 reserve는 중복되지 않는다고 나와있으므로 set 연산을 해도 그대로이다
# 만약 중복될 경우를 대비해 중복을 제거해준다
# reserve의 i-1값과 i+1 값이 lost에 포함되어 있다면 제거해준다 (왼쪽부터 제거 시작)
# 총 학생 수에서 체육복을 잃어버린 학생 수를 빼준다면 체육 수업을 들을 수 있는 학생의 수가 도출된다
# 처음에는 Dictionary를 사용하여 풀어보다가, lost[i]-1과 lost[i]+1이 reserve에 포함되었는지를 판단해서 count+=1
# 한 값을 n에서 빼주는 형식으로 풀었는데 TC 3개는 통과 했으나 실행에서 다 틀려서 위와 같이 해결했다.

# 다른사람의 풀이(3) 위와 비슷
def solution(n, lost, reserve):
    s = set(lost) & set(reserve) # lost와 reserve의 교집합(공통으로 들어있는 학생의 번호)
    l = set(lost) - s # lost에만 있는 학생 = 참가불가 학생
    r = set(reserve) - s # reserve에만 있는 학생 = 빌려줄 수 있는 학생
    
    for x in sorted(r): # reserve에서 구한 집합을 오름차순으로 정렬합니다.
        if x-1 in l: # 참가불가 학생중에 x-1인덱스가 포함되어 있다면, 그 인덱스를 삭제합니다.
            l.remove(x-1)
        elif x+1 in l: # 참가불가 학생중에 x-1이 없고, x+1에 참가불가 학생에 속해있다면, 그 인덱스를 삭제합니다.
            l.remove(x+1)

    answer = n - len(l) # 체육복 전달이 끝난 참가불가 학생 리스트의 수와 전체 학생 수의 길이를 뺴준다.
    return answer

# 위에 설명
# 두 번째 방식은, 파이썬의 set과 정렬을 이용하는 방법입니다. 알고리즘을 순서대로 표현하면 다음과 같습니다.

# 1. lost와 reserve의 교집합을 구합니다. (공통으로 들어있는 학생의 번호를 구함)
# 2. lost와 교집합의 차집합을 구합니다. (lost에만 있는 학생)
# 3. reserve와 교집합의 차집합을 구합니다. (reserve에만 있는 학생)
# 4. 3번에서 구한 집합을 정렬합니다.
# 5. 4번에서 구한 집합을 순회합니다. (여기서 체육복 전달이 이루어집니다.)
#   5.1 만약 x-1이 2번에서 구한 집합에 속할 경우, 그 원소를 삭제합니다.
#   5.2 x-1이 없을 때, x+1을 2번에서 구한 집합에 속해 있는지 확인하고 있다면, 그 원소를 삭제합니다.
# 6. 5번을 통해 구해진 잃어버린 학생들의 집합의 길이를 구하고 n에 빼줍니다.

# 체육복 정리를 잘해놓은 링크
# https://gurumee92.tistory.com/160

# 다른사람의 풀이(4) 
# 가독성이 좋은 것 같아 가져왔다. 하지만 프로그래머스에서 제출은 안된다.
def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer

# 프로그래머스 Best 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost] # 중복을 제거하는 방법은 같다. for문의 not in을 사용해서 중복제거 하기 => 빌려줄 수 있는 학생
    _lost = [l for l in lost if l not in reserve] # not in을 활용한 중복 제거 => 참가불가 학생

    for r in _reserve: # 빌려줄 수 있는 학생의 원소 추출
        f = r - 1 # 왼쪽에 있는 인덱스 [1, 2, 3, 4, 5] => ex) r이 2면 2-1 = 1, 인덱스 값 : 1 => 답은 2
        b = r + 1 # 오른쪽에 있는 인덱스 [1, 2, 3, 4, 5] => ex) r이 2면 2+1 = 3, 인덱스 값 : 3 => 답은 4
        if f in _lost: # 만약 참가불가 학생 리스트 중에 왼쪽에 있는 인덱스 값이 포함되어 있다면, 참가불가 학생 리스트에서 원소를 제거한다.
            _lost.remove(f)
        elif b in _lost: # 왼쪽에 있는 인덱스 값이 포함되어 있지않고, 오른쪽 인덱스 값에 포함되어 있다면, 참가불가 학생 리스트에서 원소를 제거한다.
            _lost.remove(b)
    return n - len(_lost) # 전체 학생 수에서 참가불가 학생 리스트의 길이를 빼준다. => 체육수업을 들을 수 있는 학생의 최댓값