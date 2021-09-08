# 문제 읽기
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수를 작성해주세요.

# s = "3people unFollowed me", return "3people Unfollowed Me"
# s = "for the last week", return "For The Last Week"

# 문제 접근
# 문자열의 첫 번째를 대문자로 바꿔준다.
# 무엇을 기준으로? 공백 기준으로
# 문자열을 공백으로 잘라서 리스트에 보관하고 첫 글자를 대문자로 변환한 후에
# 다시 join으로 붙여준다.
# title()메소드는 각 단어 제목 문자열을 활성화합니다. 
# 각 단어의 첫 문자는 대문자로 변환되고 나머지 단어 문자는 소문자로 변환됨을 의미합니다.

# 문제풀이(1)
def solution(s):
    answer = []
    message= s.split(' ') # 공백을 기준으로 문자열을 나눔
    for i in message:
        i = i.capitalize() # 첫 글자 대문자로 변환
        answer.append(i) # [문자열(1), (2), (3)]
    print(answer)
    new_Arr = ' '.join(answer) # 공백 기준으로 문자열을 붙인다.
    return new_Arr
print(solution("3people unFollowed me"))

# 문제 풀이(2)
def solution(s):
    answer = ''
    result = s.split(' ')
    for i in result:
        i = i.capitalize() # 각 단어의 앞자리를 대문자로 변환
        if answer == '':
            answer = i
        else:
            answer += ' ' + i
    return answer
print(solution("3people unFollowed me"))

# 다른사람의 Best 풀이
def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()
print(Jaden_Case("3people unFollowed me"))