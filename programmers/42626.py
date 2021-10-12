# 문제 접근
# 스코빌 지수가 K 이상으로 만들기 위해 섞어야 하는 횟수를 구해야한다. 카운팅
# 루트 값을 삭제하여 변수에 담아서 사용할 예정
# 굳이 변수에 담을 필요 없을 것 같다.
# for문을 두 번 쓰는 것은 시간초과? 조건문 제거? 변수명?

# 수도 코드(1)
import heapq

def solution(scoville, K):
    answer = 0 # 스코빌 지수 K 이상으로 되기 위해 섞은 횟수 카운팅
    heap = []
    b = 0
    for i in scoville: # 힙(heap)의 삽입 연산
        a = heapq.heappush(heap, i)
        a = heapq.heapify(heap)
    print(heap)

    for i in range(len(heap)):
        if heap[1] < heap[2]:
            b = heapq.heappop(heap) # 가장 맵지 않은 음식의 스코빌 지수 
            c = heapq.heappop(heap) # (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
            # print(b)
            # print(c)
            d = b + (c * 2) 
            heapq.heappush(heap, d)
            answer += 1
            # print(d)
            # print(heap)
    # while heap: # 힙(heap)의 삭제 연산
    #     if heap[1] < heap[2]:
    #         b = heapq.heappop(heap)
    #         c = b + 
    #         print(heap)
    #         break

    return answer
print(solution([1, 2, 3, 9, 10, 12], 7))

# 수도 코드(2)
import heapq

def solution(scoville, K):
    answer = 0 # 스코빌 지수 K 이상으로 되기 위해 섞은 횟수 카운팅
    heap = scoville # 스코빌을 heap이라는 상자에 담음
    heapq.heapify(heap) # 그 상자를 재구조화
    a = 0

    for i in heap:
        print(heap[0])
        if heap[0] < K:
            a = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
            print(a)
            heapq.heappush(heap, a)
            answer += 1
            print(a)
            print(heap)
        if len(heap) == 1 and heap[0] < K:
            return -1

    return answer
print(solution([1, 2, 3, 9, 10, 12], 7))


# 문제 풀이(1)
import heapq

def solution(scoville, K):
    answer = 0 # 스코빌 지수 K 이상으로 되기 위해 섞은 횟수 카운팅
    heap = scoville
    heapq.heapify(heap)

    while heap[0] < K:
        a = heapq.heappop(heap) + heapq.heappop(heap) * 2
        heapq.heappush(heap, a)
        answer += 1

        if len(heap) == 1 and heap[0] < K:
            return -1

    return answer
print(solution([1, 2, 3, 9, 10, 12], 7)) 

# 다른사람의 신박한 풀이(1)
import heapq

def solution(scoville, K):
    heap = []

    for i in scoville: # 힙(heap)의 삽입 연산
        heapq.heappush(heap, i)
    
    answer = 0
    while heap[0] < K: # 힙(heap)의 삭제 연산
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        answer += 1
        
    return answer