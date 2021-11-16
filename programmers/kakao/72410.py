# 문제접근
# 정규표현식을 이용한 아이디 만들기
# 맞지않으면 만들어줘야하기 때문에 변경도 생각해야 한다.

# 수도코드(1)
import re
def solution(new_id):
    # 1단계 대문자는 소문자로 치환
    answer = new_id.lower()
    # 2단계 특수문자 제거(알파벳 소문자, 숫자, 빼기, 밑줄, 마침표는 제외)
    answer = re.sub(r"[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]","", answer)
    # 3단계 마침표(...), (..)연속된 마침표는 바뀐다.
    answer = answer.replace('...', '.').replace('..', '.')
    # 4단계 아이디의 처음, 끝에 위치한 (.)은 제거된다.
    answer = answer.strip('.')
    # 5단계 빈 문자열이라면, new_id에 "a"를 대입한다.
    if answer == "":
        answer = "a"
    # 6단계 아이디의 길이가 16자 이상이므로, 처음 15자를 제외한 나머지 문자들이 제거된다.
    if len(answer) >= 16:
        answer = answer[0:15]
    # 7단계 아이디의 길이가 2자 이하라면, new_id의 마지막 문자를 길이 3이 될 때까지 반복해서 끝에 붙인다.
    while len(answer) < 3:
        answer += answer[-1]
        if len(answer) == 3: break
    return answer
print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))


# 문제풀이(1)
import re
def solution(new_id):
    # 1단계 대문자는 소문자로 표현한다. and 2단계 특수문자 제거(알파벳 소문자, 숫자, 빼기, 밑줄, 마침표는 제외)
    answer = re.sub(r"[^0-9a-z_.\-]+","", new_id.lower())
    # 3단계 마침표(...), (..)연속된 마침표를 압축해서 표현한다.
    # answer = re.sub('\.\.+','.',answer) 대체 가능 +, *은 둘다 반복 기능
    answer = re.sub('\.\.*','.',answer)
    # 4단계 아이디의 처음, 끝에 위치한 (.)은 제거된다.
    answer = answer.strip('.')
    # 5단계 빈 문자열이라면, new_id에 "a"를 대입한다.
    if answer == "":
        answer = "a"
    # 6단계 아이디의 길이가 16자 이상이므로, 처음 15자를 제외한 나머지 문자들이 제거된다.
    if len(answer) >= 16:
        answer = answer[0:15].strip('.')
    # 7단계 아이디의 길이가 2자 이하라면, new_id의 마지막 문자를 길이 3이 될 때까지 반복해서 끝에 붙인다.
    while len(answer) < 3:
        answer += answer[-1]
    return answer
print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

# 다른사람의 풀이(1)
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st