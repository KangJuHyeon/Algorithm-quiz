# 조합이란?
# 조합이란 n개의 원소를 사용해서 순서의 관계없이 r개의 배열로 나타내는 것을 말한다.
# 조합은 순서가 없어서 원소의 종류가 같으면 같은 배열로 나타낸다.

# 서로 다른 n개에서 r개를 선택할 때 순서를 고려하지 않고, 중복없이 뽑을 경우의 수

# nCr = n! / r! (n-r)!
# 예를 들어, A B C D 에서 순서를 고려하지 않고, 중복없이 2가지를 뽑는 모든 경우의 수는?
# AB/AC/AD
# BA/BC/BD
# CA/CB/CD
# DA/DB/DC
# 위에선 6가지가 된다.
# 이 때 순서를 고려하지 않기 때문에 AB와 BA는 같은 경우로 본다.

import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

# [('A', 'B'), ('A', 'C'), ('B', 'C')]

from itertools import combinations, permutations

nums = [1,2,3,4]
perm = list(combinations(nums, 2))
print(perm)

# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]