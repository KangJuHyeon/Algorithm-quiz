# 문제풀이(1)
import itertools

def solution(word):
    list1 = ['A','E','I','O','U']
    list2 = list(map(list, itertools.product('AEIOU',repeat=2)))
    list3 = list(map(list, itertools.product('AEIOU',repeat=3)))
    list4 = list(map(list, itertools.product('AEIOU',repeat=4)))
    list5 = list(map(list, itertools.product('AEIOU',repeat=5)))
    data_list = list1 + list2 + list3 + list4 + list5
    for i in range(len(data_list)):
        data_list[i] = ''.join(data_list[i])
    data_list.sort()

    return data_list.index(word)+1
print(solution("AAAAE"))  # 6
print(solution("AAAE")) # 10
print(solution("I"))    # 1563
print(solution("EIO"))  # 1189