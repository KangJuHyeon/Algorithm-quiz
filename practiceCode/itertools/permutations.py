# 순열(permutation)
# 순열이란 몇 개를 골라 순서를 고려해 나열한 경우의 수를 말한다.

# 서로 다른 n개에서 r개를 선택할 때 순서를 고려하여, 중복없이 뽑을 경우의 수
# nPr = n! / (n-r)!
# 예를 들어, A B C D에서 순서에 상관있으며, 중복없이 2가지를 뽑는 모든 경우의 수는?
# AB/AC/AD
# BA/BC/BD
# CA/CB/CD
# DA/DB/DC
# 총 12가지가 된다.
# 이때 순서를 고려하기 때문에 AB와 BA는 다른 경우로 본다.

import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

from itertools import permutations

arr = ['A', 'B', 'C']
nPr = permutations(arr, 2)
print(list(nPr))

# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# permutation 함수를 구현한 함수
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

# 위에 함수를 파이썬에선 라이브러리를 이용해 for문을 사용하지 않고도 순열을 구현할 수 있다.
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기