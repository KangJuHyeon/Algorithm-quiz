# 문제 읽기
# 네오와 프로도가 숫자놀이를 하고 있습니다.
# 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면,
# 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"

# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다.
# s가 의미하는 원래 숫자를 리턴하도록 함수를 완성해주세요.

# 문제 접근
# s 값 "one4seveneight"을 if문을 활용해서 숫자로 바꾼다.
# s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않으니, 조심
# s 안에 "four" 또는 "4"가 포함되어 있을 경우 "4"를 할당해주어라.
# replace로 바꿔버리는 게임을 해보자 간단하게
# 딕셔너리로도 풀 수 있을 것 같다. key, value

# 수도코드(1)
s = "123"
# "one4seveneight"	1478
# "23four5six7"	234567
# "2three45sixseven"	234567
# "123" 123

answer = [] # s의 값을 숫자로 변환해서 담을 변수
# 문자열
if "one" in s or "1" in s:
    answer += "1"
    print(answer)
if "two" in s or "2" in s:
    answer += "2"
    print(answer)
if "three" in s or "3" in s:
    answer += "3"
    print(answer)
if "four" in s or "4" in s:
    answer += "4"
    print(answer)
if "five" in s or "5" in s:
    answer += "5"
    print(answer)
if "six" in s or "6" in s:
    answer += "6"
    print(answer)
if "seven" in s or "7" in s:
    answer += "7"
    print(answer)
if "eight" in s or "8" in s:
    answer += "8"
    print(answer)
if "nine" in s or "9" in s:
    answer += "9"
    print(answer)

# print(s)
print("".join(answer))

# 문제풀이(1)
def solution(s):
    answer = [] # s의 값을 숫자로 변환해서 담을 변수
    # 문자열
    if "one" in s or "1" in s:
        answer += "1"
        print(answer)
    if "two" in s or "2" in s:
        answer += "2"
        print(answer)
    if "three" in s or "3" in s:
        answer += "3"
        print(answer)
    if "four" in s or "4" in s:
        answer += "4"
        print(answer)
    if "five" in s or "5" in s:
        answer += "5"
        print(answer)
    if "six" in s or "6" in s:
        answer += "6"
        print(answer)
    if "seven" in s or "7" in s:
        answer += "7"
        print(answer)
    if "eight" in s or "8" in s:
        answer += "8"
        print(answer)
    if "nine" in s or "9" in s:
        answer += "9"
        print(answer)
    answer = "".join(answer)
    print(answer)
    return int(answer)
print(solution("one4seveneight"))

# 문제 풀이(2)
def solution(s):
    answer = s 
    answer = answer.replace('zero', '0')
    answer = answer.replace('one', '1')
    answer = answer.replace('two', '2')
    answer = answer.replace('three', '3')
    answer = answer.replace('four', '4')
    answer = answer.replace('five', '5')
    answer = answer.replace('six', '6')
    answer = answer.replace('seven', '7')
    answer = answer.replace('eight', '8')
    answer = answer.replace('nine', '9')

    return int(answer)

# 딕셔너리를 이용해서 위 내용 수정해보기
# 문제풀이(3)
def solution(s):
    string = {
            'zero': 0, 'one': 1, 'two': 2, 
            'three': 3, 'four':4, 'five':5, 
            'six':6, 'seven':7, 'eight':8, 
            'nine':9
            }

    answer = s
    for i in string.items(): # Key, Value 쌍 얻기(items)
        # print(i, ':', string[i])
        answer = answer.replace(i[0], str(i[1]))
        # print(i[0]) # key 값
        print(str(i[1])) # value 값
    return int(answer)
print(solution("one4seveneight"))

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"

# 지인이 추천한 방식
# 문제풀이(4)
def solution(s):
    string = {
            'zero': 0, 'one': 1, 'two': 2, 
            'three': 3, 'four':4, 'five':5, 
            'six':6, 'seven':7, 'eight':8, 
            'nine':9
            }
    answer = s
    for item in string:
        answer = answer.replace(item, str(string.get(item))) # str(string.get(item)) => 키 값을 조회해서, value 값을 얻는 방법
        print(str(string.get(item)))
    return int(answer)
print(solution("one4seveneight"))

# 다른사람이 푼 Best 방식
num_dic = {
    "zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", 
    "six":"6", "seven":"7", "eight":"8", "nine":"9"
    }

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)