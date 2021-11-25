# 문제접근
# "CBD"가 선행스킬이니, 유저들의 스킬트리 중 B,D가 먼저 나온다면 불가능한 스킬트리, CBD순으로 잘 나왔다면 가능한 스킬트리 알림
# 테스트케이스가 CBD가 아닐 때를 생각해야된다. 모든 요소를 확인하면서 가능, 불가능을 판단해야된다.

# 수도코드(1)
def solution(skill, skill_trees):
    answer = 0 # 가능한 스킬트리의 갯수 카운팅
    for i in range(len(skill)):
        for j in range(len(skill_trees)):
            if skill[i] in skill_trees[j]:
                if skill_trees[j].find('C') < skill_trees[j].find('B'):
                    answer += skill_trees[j].find('C')
                    print("가능한 스킬트리입니다.")
                else:
                    print("B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. \n불가능한 스킬트리입니다.")
        break
    return answer
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2

# 문제풀이(1)
def solution(skill, skill_trees):
    answer = 0 # 가능한 스킬트리의 갯수 카운팅
    for i in skill_trees: # BACDE, CBADF
        word = '' # 스킬트리 초기화
        for j in i: # B, A, C, D, E
            if j in skill: # CBD가 j에 포함되어 있다면
                word += j # BCD

        if skill[:len(word)] == word: # CBD == BCD
            answer += 1

    return answer
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2

# 문제풀이(2)
def solution(skill, skill_trees):
    answer = 0 # 가능한 스킬트리의 갯수 카운팅
    for i in skill_trees:
        result = []
        judgment = True

        for j in range(len(i)):
            if i[j] in skill:
                result.append(i[j])

        for k in range(len(result)):
            print(skill[k])
            if result[k] != skill[k]:
                judgment = False
                break
        
        if judgment == True:
            answer += 1

    return answer
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2


# 이 문제에 대한 테스트케이스 list
print(solution("CBD", ["CAD"])) # 0
print(solution("CBD", ["AEF", "ZJW"])) # 2
print(solution("REA", ["REA", "POA"])) # 1
print(solution("CBDK", ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"])) # 4
print(solution("BDC", ["AAAABACA"])) # 0
print(solution("CBD", ["C", "D", "CB", "BDA"])) # 2
