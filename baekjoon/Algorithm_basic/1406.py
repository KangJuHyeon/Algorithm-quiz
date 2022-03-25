# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함

import sys 
stack_1 = list(sys.stdin.readline().rstrip())
stack_2 = []

for i in range(int(sys.stdin.readline())):
    temp = list(sys.stdin.readline().split())
    print(temp)
    if temp[0] == "L":
        if stack_1:
            stack_2.append(stack_1.pop())
            print(stack_2)
    elif temp[0] == "D":
        if stack_2:
            stack_1.append(stack_2.pop())
            print(stack_1)
    elif temp[0] == "B":
        if stack_1:
            stack_1.pop()
            print(stack_1)
    else:
        stack_1.append(temp[1])
        print(stack_1)
stack_1.extend(reversed(stack_2))
print(''.join(stack_1))
            
    