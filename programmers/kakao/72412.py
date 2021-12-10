# 수도코드(1)
import re
def solution(info, query):
    answer =[]
    info_key_dict = {}
    query_key_dict = {}
    
    for i in info:
        regex_box = [] # 점수를 담을 상자
        query_regex = i.rsplit(' ', 1) 

        if query_regex[0] in info_key_dict: # info_key_dict에 query_regex 0번째 문자열이 포함되어 있다면
            values_box = info_key_dict[query_regex[0]] # info_dict 0번째를 key 삽입, 
            values_box.append(int(query_regex[1])) # info_dict에 1번째 점수를 int로 변환하여 values로 삽입
            info_key_dict[query_regex[0]] = values_box # 배열을 딕셔너리에 삽입
        else:
            regex_box.append(int(query_regex[1]))
            info_key_dict[query_regex[0]] = regex_box
    print(info_key_dict)
    print(regex_box)
    
    for i in query:
        query_regex = i.replace('and', '').split()
        regex = ''
        for j in range(len(query_regex)-1):
            if not '-' == query_regex[j]:
                temp = "(?=.*" + query_regex[j] + ")"
                # print(temp)
                regex += temp
        
        query_key_dict[regex] = int(query_regex[4]) # 점수만 빼옴
        # print(query_key_dict[regex])

    for key, values in query_key_dict.items(): # query_key
        count = 0
        dict_regex = re.compile(key) # dict_regex와 result가 regex
        # print(dict_regex)
        for info_key, info_values in info_key_dict.items(): # info_key
            result = dict_regex.match(info_key) # query_key와 info_key와 match한 후
            # print(result)
            if None != result: # result가 None 값이 아니라면 
                for regex_box in info_values: # info_values의 값이 regex_box 값에 포함되어 있다면
                    if values <= regex_box:
                        count += 1
        
        answer.append(count)
    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

# 수도코드(2)
import re
def solution(info, query):
    answer = [] 
    info_dict = {}
    count = 0

    for i in info:
        regex_box = [] # 점수를 담을 상자
        query_regex = i.rsplit(' ', 1) 

        if query_regex[0] in info_dict: # info_key_dict에 query_regex 0번째 문자열이 포함되어 있다면
            values_box = info_dict[query_regex[0]] # info_dict 0번째를 key 삽입, 
            values_box.append(int(query_regex[1])) # info_dict에 1번째 점수를 int로 변환하여 values로 삽입
            info_dict[query_regex[0]] = values_box # 배열을 딕셔너리에 삽입
        else:
            regex_box.append(int(query_regex[1]))
            info_dict[query_regex[0]] = regex_box
    print(info_dict)
    
    query_box =[]
    score = []
    query_dict = {}
    for i in query:
        query_regex_key = i.rsplit(' ', 1)
        score.append(int(query_regex_key[1]))
        query_regex_key = i.replace('and', '') # and 제거, 모든 공백 제거
        query_regex_key = re.sub('[-]', '', query_regex_key) # -는 고려하지 않으므로, 그냥 제거하기로 함
        query_box.append(''.join(query_regex_key))
        query_dict[query_box[0]] = query_box
    print(query_dict)

    for info_key, info_values in info_dict.items():
        if info_key in query_box:
            print('포함되어 있어요ㅠㅠ')
            # if info_values >= score:
                # count += 1
                    
        answer.append(count)
    
    print(query_box)
    print(score)

    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

# 수도코드(3)
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        infol = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
        mykey = infol[:-1]  # info의 점수제외부분을 key로 분류
        myval = infol[-1]  # info의 점수부분을 value로 분류

        for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for c in combinations(mykey, j):
                tmp = ''.join(c)
                print(tmp)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))  # 그 조합의 key값에 점수 추가
                else:
                    info_dict[tmp] = [int(myval)]
    
    for k in info_dict:
        info_dict[k].sort()  # dict안의 조합들을 점수순으로 정렬

    for qu in query:  # query도 마찬가지로 key와 value로 분리
        myqu = qu.split(' ')
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while 'and' in qu_key:  # and 제거
            qu_key.remove('and')
        while '-' in qu_key:  # - 제거
            qu_key.remove('-')
        qu_key = ''.join(qu_key)  # dict의 key처럼 문자열로 변경
        # print(qu_key)
        if qu_key in info_dict:  # query의 key가 info_dict의 key로 존재하면
            scores = info_dict[qu_key]
            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, int(qu_val))
                # print(enter)
                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
