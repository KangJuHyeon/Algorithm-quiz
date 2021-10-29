# 문제 접근
# stack? Queue의 형식을 사용해서 ((구명보트의 타고 있는 사람의 무게) + (구명보트에 탈 예정인 사람 무게)) >= (한 사람의 몸무게)
# 위에 형식으로 구명보트를 카운팅할 예정이다.
# 비슷하게 풀어봤지만 효율성 문제에서 빨간색이였다.
# 다른 방법으로 deque, 비교하기 등의 문제로 풀어봐야겠다.

# 수도코드(1)
def solution(people, limit):
    people.sort(reverse=True)
    boat = []
    count = 0 # 모든 사람을 구출하기 위해 필요한 구명보트의 최소 갯수 카운팅
    print(boat)
    for i in people:
        while len(boat) >= 0:
            if people:
                if sum(boat) + people[0] <= limit:
                    boat.append(people.pop(0))
                    print(boat)
                else:
                    boat.pop(0)
                    count += 1
                    print(count)
            else:
                if boat != []:
                    count += 1
                    print(boat)
                break

            print(boat)

    return count
print(solution([70, 50, 80, 50], 100)) # 3
print(solution([70, 80, 50], 100)) # 3

# 수도코드(2)
from collections import deque

def solution(people, limit):
    arr = []
    answer = None
    for i in people:
        arr.append(i)
        arr.sort()

    dp = deque(arr)
    count = 0
    while dp:
        print(dp)
        if len(dp) == 1:
            count += 1
            break
        else:
            print(dp)
            if dp[0] + dp[-1] <= limit:
                dp.popleft()
                dp.pop()
                count += 1
                print(count)
                print(dp)
            else:
                dp.pop()
                count += 1

    return count
print(solution([70, 50, 80, 50], 100)) # 3
print(solution([70, 80, 50], 100)) # 3


# 문제풀이(1)
from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    count = 0
    while people:
        if len(people) == 1:
            count += 1
            break
        else:
            if people[0] + people[-1] <= limit:
                people.popleft()
                people.pop()
                count += 1
            else:
                people.pop()
                count += 1

    return count
print(solution([70, 50, 80, 50], 100)) # 3
print(solution([70, 80, 50], 100)) # 3

# 다른사람의 풀이(1)
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer

# 다른사람의 풀이(2)
def solution(people, limit):
    answer = len(people)
    p = sorted(people,reverse = True)
    s,e = 0, len(p)-1
    while s < e : 
        if p[s]+p[e] <= limit :
            e-=1
            answer-=1
        s+=1
    return answer
