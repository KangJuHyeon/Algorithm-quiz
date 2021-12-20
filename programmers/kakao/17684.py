# 문제풀이
# LZW 알고리즘 구현하는 문제.
# 딕셔너리에 A-Z까지 담아주고, 그 번호에 따른 값을 배열에 넣어주면 해결?
# 가장 긴 문자열 w를 어떻게 찾아야할까 => 함수 사용?
# 현재 입력 + 다음 단어의 인덱스가 없을 경우
# W(현재입력)의 index의 배열을 저장하고, w+c 조합을 index에 삽입한다.
# w(현재입력)에 다음 단어를 대입해야한다.

# 수도코드(1)
def solution(msg):
    answer = []
    dict = {}
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(1, len(alpha)+1):
        dict[string[i-1]] = i
    for i in msg:
        for j in dict.items():
            if j[0] == i:
                answer.append(j[1])
    
    return answer
print(solution('KAKAO')) # [11, 1, 27, 15]
print(solution('TOBEORNOTTOBEORTOBEORNOT')) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution('ABABABABABABABAB')) # [1, 2, 27, 29, 28, 31, 30]

# 문제풀이(1)
def solution(msg):
    answer = []
    dict = {}
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # 딕셔너리에 A-Z까지 담아준다.
    for key, value in enumerate(alpha, start=1):
        dict[value] = key
        new_idx = key
    print(dict)
    # 가장 긴 문자열 w를 찾는 과정이 필요하다.
    w = msg[0] # 현재 단어 대입
    idx = 1 # 다음 단어(c)
    while idx < len(msg):
        # 만약 w + msg[1]의 값이 dict에 포함되어 있지 않다면
        if w + msg[idx] not in dict:
            answer.append(dict[w])
            new_idx += 1
            dict[w + msg[idx]] = new_idx
            # 다음 단어로 저장해야된다.
            w = msg[idx]
            # 다음 단어로 넘어가기 위해 카운팅
            idx += 1
            continue
        # 이미 색인되어 있는 단어의 경우, 다음 단어를 현재 입력에 추가
        w += msg[idx]
        idx += 1
    answer.append(dict[w])

    return answer
print(solution('KAKAO')) # [11, 1, 27, 15]

# 다른사람의 풀이(1)
def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer

# 다른사람의 풀이(2)
def solution(msg): 
    answer = [] 
    new_id = 27 
    word_dict = dict() 
    
    for ascii_num in range(65, 91): 
        word_dict[chr(ascii_num)] = ascii_num - 64 
        idx_f, idx_e = 0, 0 
        
        while True: 
            idx_e += 1 
            if idx_e == len(msg): 
                answer.append(word_dict[msg[idx_f:idx_e]]) 
                break 
            
            if msg[idx_f:idx_e+1] not in word_dict.keys(): 
                word_dict[msg[idx_f:idx_e+1]] = new_id new_id += 1 
                answer.append(word_dict[msg[idx_f:idx_e]]) 
                idx_f = idx_e 
    
    return answer
