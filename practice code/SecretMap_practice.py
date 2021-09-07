# 수도코드(1)
def solution(n, arr1, arr2):
    # 제곱의 값을 어떻게 표현을 해야할지?
    # arr1 i값과 arr2 j값과 i + j = 39 => 큰 수에서 어떠한 수를 제곱한 수를 뺄건대 <=
    # 이걸 어떻게 표현할지?
    answer = []
    arr = []
    a = [16, 8, 4, 2, 1]
    b = '#'
    c = 0 # 값을 저장할 변수

    for i in range(n): # 1,2,3,4,5
        # print(i)
        score = arr1[i] + arr2[i]
        answer.append(score) # sum arr [39, 21]

    for i in answer:
        # print(i)
        result = []
        for j in a:
            if i - j: # 39 - 16 = 23, 21 - 16 = 5
                # print(i - j)
                c = i - j
                result.append(b)
    # arr.append("".join(result))
    return arr
print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))

# 수도코드(2)
def solution(n, arr1, arr2):
    answer = []
    result = []
    a = [16, 8, 4, 2, 1]

    for i in range(n): # 1,2,3,4,5 arr1,arr2를 더한 값을 구하려는 곳
        score = arr1[i] + arr2[i]
        answer.append(score) # [39, 21, 49, 35, 39]
    print(answer)

    for i in answer: # [39, 21, 49, 35, 39] => 39, 21, 49, 35, 39 => 2진법으로 변환?
        b = []
        for j in a: # 16, 8, 4, 2, 1
            if i - j < 0: 
                b.append(None)
                continue
            else:
                i = i - j
                b.append(i)
        c = []
        for k in range(len(b)):
            if b[k] is None:
                c.append(" ")
            else:
                c.append("#")
            # c.append("".join(c))
        result.append("".join(c))
    # print(result)
    return result
        
print(solution(5, [9,20,28,18,11], [30,1,21,17,28])) 

# 수도코드(3)
def solution(n, arr1, arr2):
    answer = []
    result = []
    a = [16, 8, 4, 2, 1]
    b = []

    for i in range(n): # 1,2,3,4,5 arr1,arr2를 더한 값을 구하려는 곳
        score = bin(arr1[i]) # 2진법으로 arr1[i]를 변환
        score2 = bin(arr2[i]) # 2진법으로 arr2[i]를 변환
        print(score)
        print(score2)
        score = format(score, 'b') # 2진법으로 변환
        print(score)
        answer.append(score) # ['100111', '10101', '110001', '100011', '100111'] 
    print(answer)

    for i in answer: # arr1[i] + arr2[i] 값을 #과 공백으로 나눠준다.
        if i == 0:
            b.append(" ")
        else:
            b.append("#")
    result.append("".join(b))
    print(result)
    return result
        
print(solution(5, [9,20,28,18,11], [30,1,21,17,28])) 

# 수도코드(4)
def solution(n, arr1, arr2):
    max = (2 ** n) - 1
    result = []

    for i in range(n):
        result_sum = arr1[i] + arr2[i]
        if result_sum >= max:
            result.append(max)
        else:
            result.append(result_sum)
    print(result)

    for i in result:
        d = format(i, "b")
        print(d)
        
print(solution(5, [9,20,28,18,11], [30,1,21,17,28])) 