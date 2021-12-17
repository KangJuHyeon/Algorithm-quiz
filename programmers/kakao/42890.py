# 문제풀이(1)
from itertools import combinations
def solution(relation):
    answer = 0
    row = len(relation) # 튜플 개수
    col = len(relation[0]) # 속성 개수
    
    # 전체 조합
    combo = []
    for i in range(1, col+1): # 속성 list 1부터 시작
        combo.extend(combinations(range(col), i)) # 조합 리스트 구하기, 종목별로 만들 수 있는 모든 조합갯수 찾기
        # print(combo)
    
    # 유일성
    unique = []
    for i in combo:
        temp = [tuple([item[j] for j in i]) for item in relation] # 주어진 키로 리스트의 index별 아이템 뽑아내기
        # print(temp)
        if len(set(temp)) == row: # 만약 set로 변경후 사라진게 없다면 key로 사용해도 무방하다.
            unique.append(i)
            print(unique)
    
    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])): # key 중에 겹치는 부분이 있는 것을 삭제(최소성을 위해)
                answer.discard(unique[j])
                
    return len(answer)
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
