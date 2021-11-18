# 문제접근
# 결국 이 문제는 k층 n호에 몇명의 사람이 살고 있는지 구하는 문제이다.
# 3층 4호에 살고있는 사람을 구하려면 2층 1,2,3,4호 사람들을 더한 값이 3층 4호에 살고있는 사람이 된다.
# 0층 1,2,3,4호부터 값을 구한 뒤 1층 1호, 2호, 3호, 4호를 천천히 구해본다.

T = int(input()) # TestCase 갯수

for i in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    # 결과 값 : k층 n호에 몇명이 살고 있는가?
    people = [i for i in range(1, n+1)] # 0층에서 1부터 n호까지의 각각 사람의 수를 리스트에 담는다.
    # print(people)
    
    # 1층, 2층, 3층, 4층
    for j in range(k): # k층에 있는 사람들의 수를 데려와야 한다.
        # 1호, 2호, 3호, 4호
        for l in range(1, n):
            people[l] += people[l-1]
            # print(people)
    print(people[-1])
