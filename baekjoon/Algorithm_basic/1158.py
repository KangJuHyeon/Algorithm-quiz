# 우선순위 큐 구현

from queue import PriorityQueue

p = PriorityQueue()
print(dir(p))
q1 = PriorityQueue(maxsize=10)
print(dir(q1))

from collections import deque

N, K = map(int, input().split())

# 우선순위 큐에서 몇 번쨰를 제거할에 대한 숫자를 대입하여 뺸다.
priorityQueue = deque([])
for i in range(1, 1+N):
    priorityQueue.append(i)
    print(priorityQueue)

# 새로 맞춰질 우선순위 배열
result = []
while len(priorityQueue) != 0:
    print(priorityQueue)
    for i in range(K-1):
        priorityQueue.append(priorityQueue.popleft())
        print(priorityQueue)
    result.append(priorityQueue.popleft())
    print(result)

# <3, 4,> 구현
print("<", end="")
for i in range(len(result)):
    print(result[i], end="")
    if i != len(result)-1:
        print(", ",end="")
print(">", end="")