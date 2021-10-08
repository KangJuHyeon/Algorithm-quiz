# bridge_length = 2, weight = 10, truck_weights = [7, 4, 5, 6], return = 8

# 문제 접근
# 첫 번째 트럭이 들어가서 첫 번째로 나오기 때문에 Queue 방식으로 푸는 것이 맞다고 생각했다.
# 큐에서 빠져나온 다리를 지난 트럭들은 따로 담는 상자를 선언
# 초를 세야하니 반복문 안에 다리를 지난 트럭들이 상자에 담길 때 카운팅을 추가한다.
# 다리를 지난 트럭, 다리를 건너는 트럭을 선언?
# 다리를 지나는데 다리에 몇 대의 트럭이 있는지까지 세야되는 것 같다.
# 다리에 2개 이상의 트럭이 들어와 있을 때? [0, 0]

# 수도코드(1)
from collections import deque

def solution(bridge_length, weight, truck_weights):
    n = deque(truck_weights) # 트럭별 무게를 큐로 선언
    answer = [] # 다리를 지난 트럭을 넣어줄 상자 선언
    count = 0 # 트럭들이 다리를 지날때마다 카운팅할 카운트 선언
    print(n)
    
    while n:
        count += 1
        truck_weights = n.popleft() # 대기중인 트럭에서 한대를 빼고 그대로 다리를 건너는 트럭에 넣는다.
        print(truck_weights)
        print(count)
        for i in n: # [4, 5, 6] 부터 시작
            print(i)
            print(count)
            if truck_weights > i:
                count += 1
                break
            else:
                count += 1
        answer.append(truck_weights) # 다리를 지난 트럭에 추가
        print(answer)

    return count
print(solution(100, 100, [10]))
# 2, 10, [7,4,5,6]
# 100, 100, [10]
# 100, 100, [10,10,10,10,10,10,10,10,10,10]



# 문제풀이(1)
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length # [0, 0] <= [트럭, 0] <= [0, 트럭] 현재 다리 길이만큼
    count = 0 # 트럭들이 다리를 지날때마다 카운팅할 카운트 선언
    print(bridge)
    
    while len(bridge):
        count += 1
        print(count)
        bridge.pop(0) # [0]
        print(bridge)
        if truck_weights: # [7, 4, 5, 6]
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
                print(bridge) # [0, 7]
            else:
                bridge.append(0)
                print(bridge)  
        print(bridge)

    return count
print(solution(2, 10, [7,4,5,6]))