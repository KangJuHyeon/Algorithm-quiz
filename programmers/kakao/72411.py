# 문제 이해
# "단품메뉴 조합이 몇 번 나왔느냐"에 따라서 코스요리 메뉴 구성 후보를 정해야한다.
# 1번, 2번, 4번, 6번 손님으로부터 A, C라는 단품메뉴가 4번 주문됐습니다.
# 3번, 4번, 6번 손님으로부터 C, D, E라는 단품메뉴가 3번 주문됐습니다.
# 위에 방식대로 result에 코스요리 메뉴 구성 후보를 담으면 된다.

# 문제접근
# course배열을 먼저 돌고, orders의 배열에서 단품 메뉴가 2개, 3개, 4개가 똑같은 사람을 카운팅한다.
# 딕셔너리를 사용하는 것과 배열에 들어가기 전에 카운팅하고 담는 2가지 방법이 떠올랐다.
# 중복된 메뉴들을 찾아야한다.
# 각 조합의 메뉴마다 몇개가 나왔는지를 알아야할 것 같다. 너무어렵다.
# AB, ABC, ABCF, ABCFG 몇개 이런식으로 풀어야할 것 같은데 다른 방법이 있을까
# Counter 라이브러리, combinations 라이브러리를 사용 가능할 것 같다.
# 함수를 2개? 그리고 딕셔너리를 사용안해도 Counter함수가 딕셔너리로 이루어져 있기 때문에 굳이 사용할 필요 없다.

# 문제풀이 과정 정리
# 1. 각 메뉴별로 모든 조합을 만들어야 한다. 그러니 조합을 만든 개수를 담은 course를 순회한다.
# 2. 조합하려는 개수를 선정했다면 orders에 있는 원소들로 조합한다. AB, ABC, ABCD, ABCDF
# 3. 가능한 조합을 만들고, 그 조합이 몇개가 등장하는 지 카운팅해야한다. => 딕셔너리를 사용해도 좋고, Couter 라이브러리를 사용해도 좋다.
# 4. 그렇다면 조합 당 몇개가 있는지 확인할 수 있을 것이다. 여기서 매우 어려웠다.
# 5. 만약 0이 아니라면 딕셔너리의 keys 값들 중 max count 값의 문자열을 가져와서 join을 시키면 finish
# 5. value 중에 카운팅이 가장 많이 되어있는 것을 오름차순으로 정렬해서 box에 담는다.
# 6. 그 box 중에 value 값이 제일 많은 값들 중에 keys들만 뽑아서 answer에 join해서 담는다.
# 5번에서 Couter함수를 사용해서 제일 많이 나온 문자들을 구했다면, 조건식을 가볍게 쓸 수 있다, 
# 하지만 그렇게 하지않고 배열에 담았다면, 그 배열에서 max값을 따로 구해서 딕셔너리 key값을 구해야 된다.

# 문제풀이(1)
from collections import Counter
from itertools import combinations

def solution(orders, course):
    # 만약에 코스요리가 2개일 때, 1번, 2번, 4번, 6번 손님으로부터 4번 주문을 받았을 때
    # 만약에 코스요리가 3개일 때,
    # 만약에 코스요리가 4개일 때,
    answer = [] # result, 코스요리 메뉴 구성 후보를 담을 빈 배열
    for i in course:
        new_menu = [] # 새로운 메뉴들을 담는다. AB, ABC, ABCD
        for j in orders:
            combo = combinations(sorted(j), i) # 조합한다.
            new_menu += combo # 조합한 메뉴들을 상자에 담는다.
            # print(new_menu)
        menu_count = Counter(new_menu) # AB가 몇개인지, ABC가 몇개인지 카운팅
        # 잘만들면 풀린다. 조건식을 모르겠다.
        if menu_count: # 만약 menu_count일 때, 가장 큰 값들을 가져오면 된다. 맨 앞의 값, 오름차순 값들
            max_count_combo = max(list(menu_count.values()))
            if max_count_combo >= 2: # course는 2이상 10이하
                for key, value in menu_count.items():
                    if menu_count[key] == max_count_combo:
                        answer.append(''.join(key))
    return sorted(answer)
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))

# 문제풀이(2)
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        new_menu = []
        for j in orders:
            combo = combinations(j, i)
            for k in combo:
                menu = ''.join(sorted(k))
                new_menu.append(menu)
                print(new_menu)
        count_menu = Counter(new_menu).most_common() # 많은 메뉴들부터 정렬
        # 잘만들면 풀린다. 조건식을 모르겠다.
        for key, values in count_menu:
            print(count_menu[0][1])
            if values == count_menu[0][1]:
                answer.append(''.join(key))
    return sorted(answer)
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))