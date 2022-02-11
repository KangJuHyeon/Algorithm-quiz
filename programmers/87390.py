# 문제접근
# 주어진 과정대로 만들어진 1차원 배열을 리턴하라.
# 입력으로 주어지는 n 숫자 ⇒ n * n 행렬을 만든다.
# 숫자를 채워넣는다.
# 행렬을 1 * n^2의 배열로 재배치한다. 한줄로 재배치
# 입력으로 주어지는 left ~ right까지의 index에 써진 숫자를 반환한다.

# 수도코드(1)
def newArr(a):
    return a + 1

def solution(n, left, right):
    # 1. n행 n열 크기의 비어있는 2차원 배열을 만든다.
    # arr = [list(range(n)) for _ in range(n)]
    # 2차원 배열을 만드는 과정을 잘 생각해야 된다.
    arr1 = []
    arr = [ i for i in range(1, n+1)]
    arr1.extend(arr)
    # print(arr1)
    
    for i in range(1, n):
       arr[:i] = list(map(newArr, arr[:i]))
    #    print(arr[:i])
       arr1.extend(arr)
       print(arr)
        
            
    return arr1[left:right+1]
print(solution(3, 2, 5)) # [3,2,2,3]
print(solution(4, 7, 14)) # [4,3,3,3,4,4,4,4]

# 문제풀이(1)
def solution(n, left, right):
    results = []
    for x in range(left, right+1):
        # divmod(3, 2), divmod(7, 4) => (1, 3)
        results.append(max(divmod(x, n)) + 1)
        # results.append(divmod(x, n))
        print(results)
    return results
print(solution(3, 2, 5)) # [3,2,2,3]
print(solution(4, 7, 14)) # [4,3,3,3,4,4,4,4]

# 다른사람의 풀이(1)
# NOTE 문제풀이(1) 코드와 똑같지만 함수의 여부만 다름
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer