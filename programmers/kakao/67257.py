# 문제 접근
# 연산자 우선순위를 정했을 때, 가장 큰 절댓값을 얻을 수 있다.
# [+,-,*]을 조합해서 결과값을 도출해보고, 정규표현식을 사용해볼 수 있을 것 같다.

import re
from itertools import permutations

def solution(expression):
    answer = 0
    combo = list(permutations(['+','-','*'], 3))
    expression = re.split('([-+*])', expression)

    result = []
    for i in combo:
        cb = expression[:]
        # print(cb)
        for j in i:
            while j in cb:
                idx = cb.index(j)
                print(idx)
                cb[idx-1] = str(eval(cb[idx-1] + j + cb[idx+1]))
                print(cb[idx-1])
                del cb[idx:idx+2]
        result.append(abs(int(cb[0])))
    return max(result)
print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))