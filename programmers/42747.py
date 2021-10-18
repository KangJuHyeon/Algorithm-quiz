# 문제 접근
# h-index가 무엇인지? 계산하는 방법을 알아야봐야 된다.
# 피인용 횟수가 논문의 순번보다 작아지기 시작하는 직전의 순번이 연구자의 h-index가 됩니다.

# 수도코드(1)
def solution(citations):
    answer = sorted(citations, reverse=True)
    h = 0 # h-index의 값을 구하고 넣을 상자 선언
    for key,value in enumerate(answer):
        print(key,value)
        if value == 0:
            return h
        if key > value:
            h = key# h-index 계산한 값을 구함
            print(h)
    return h
print(solution([3, 0, 6, 1, 5])) # 3
print(solution([9, 7, 6, 2, 1])) # 3
print(solution([10, 8, 5, 4, 3])) # 4
print(solution([25, 8, 5, 3, 3])) # 3

# 수도코드(2) 
# 테스트 코드 9번 통과 x 
# => 마지막 return에 len(citations) 해주면 통과
def solution(citations):
    answer = sorted(citations, reverse=True)
    h = 0 # h-index의 값을 구하고 넣을 상자 선언
    for key,value in enumerate(answer):
        if key >= value:
            return key
    return 0
print(solution([3, 0, 6, 1, 5])) # 3
print(solution([9, 7, 6, 2, 1])) # 3
print(solution([10, 8, 5, 4, 3])) # 4
print(solution([25, 8, 5, 3, 3])) # 3

# 문제풀이(1)
def solution(citations):
    citations.sort(reverse=True)
    h = 0 # h-index의 값을 구하고 넣을 상자 선언
    for key,value in enumerate(citations):
        # print(key, value)
        if key >= value:
            return key
        # print(len(citations))
    return len(citations)
print(solution([3, 0, 6, 1, 5])) # 3
print(solution([9, 7, 6, 2, 1])) # 3
print(solution([10, 8, 5, 4, 3])) # 4
print(solution([25, 8, 5, 3, 3])) # 3

# 문제풀이(2)
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    h = 0 # h-index의 값을 구하고 넣을 상자 선언
    for i in range(len(citations)):
        if i+1 <= citations[i]:
            h = i+1
    return h
print(solution([3, 0, 6, 1, 5])) # 3
print(solution([9, 7, 6, 2, 1])) # 3
print(solution([10, 8, 5, 4, 3])) # 4
print(solution([25, 8, 5, 3, 3])) # 3