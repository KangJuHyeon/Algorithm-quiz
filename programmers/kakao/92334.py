# 문제접근
# k번 이상 신고된 유저는 게시판 이용이 정지가 되고, 정지 사실을 메일로 발송
# 각 유저별로 처리 결과 메일을 받은 횟수를 리턴받음 [2,1,1,0]

# 문제풀이(1)
from collections import defaultdict

def solution(id_list, report, k):
    answer = {}
    box = [] # 유저 순서대로 신고 당한 수 
    singo = {} # 신고당한 사람: 신고한 사람 수
    # print(id_list)
    # print(report)

    for i in id_list:
        singo[i] = []
        print(singo[i])
        answer[i] = 0 # 초기 신고 값을 0을 넣어준다.
        print(answer)

    # 신고한 사람의 리스트, "신고한 유저 신고 당한 유저"
    for i in report:
        a, b = i.split(' ') # 신고하는 유저와 신고 당하는 사람을 공백으로 분리
        print(a, b)
        print(singo[b])
        if a not in singo[b]: 
            singo[b].append(a)
            print(singo[b])
    print(singo.values())
    for i in singo.values(): # 유저별로 신고 당한 횟수를 저장함
        box.append(len(i))
        print(box) # muzi: 1번 신고당함, frodo: 2번 신고당함, apeach: 0번 신고당함, neo: 2번 신고당함

    for key, value in enumerate(box):
        print(key, value)
        if value >= k: # 만약 value가 k번 이상일 때
            print(singo[id_list[key]]) # 누구에게 신고당했는지 알수있는 리스트
            for i in singo[id_list[key]]: 
                answer[i] += 1 # 신고한 사람에게 +1씩
                print(answer[i])

    # for i in report:
    #     word = i.split(' ')
    #     uid = word[0] # 유저 id
    #     repo = word[1] # 이 유저가 신고한 사람
    #     print(uid)
    #     # print(repo)
    #     # if repo == k: # 만약 신고당한 유저가 k번 신고당했다면
    #     dict[uid] = repo
    #     print(dict)

    # 결국 신고한 사람이 받아야된다는 소린대, muzi가 두명 신고했는데 둘다 k번 이상 신고받아서 정지되었으면 두명 다 정지되었다고 메일이 와야된다는 소린대...
    # 3명 신고했는데 그 중 2명 정지되었다면 2명만 정지되었다고 메일이 나한테 와야한다.
    return list(answer.values()) 
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

# 다른사람의 풀이(1)
from collections import defaultdict

def solution(id_list, report, k):
    answer = list()
    count = defaultdict(int)   # 몇번 신고했는지
    user = defaultdict(set)  # 신고 리스트
    # 1. 누가 누구를 신고했는지 dict 담기 & 신고당한 횟수 세기
    for r in report:
        a, b = r.split()  # a가 b를 신고
        if b not in user[a]:   # 같은 사람이 1번 이상 신고 x
            user[a].add(b)
            count[b] += 1  # 신고당한 수
    # 2. 이용자별로 자신이 신고한 사람이 k번 이상이면 처리된 횟수 + 1
    for id in id_list:
        result = 0
        for u in user[id]:
            if count[u] >= k:
                result += 1
        answer.append(result)
    return answer
