def solution(participant, completion):
    answer = '' # 문자열을 입력받는 부분(key)
    temp = 0 
    dic = {} # 객체를 선언
    for part in participant:	# 참가자들의 리스트
        dic[hash(part)] = part # 객체에 해시함수를 사용하여 part라는 임의 값(문자열)을 int형 정수 고정 길이로 변환하는 것
        temp += int(hash(part)) # 정수형 해시값을 temp라는 값과 더하여 할당

    for com in completion:  # 완주자들의 리스트
        temp -= hash(com)	# 완주자들의 이름의 해시값들을 temp에서 빼준다.
        answer = dic[temp]		# 그렇다면 temp에는 하나의 이름에 대한 해시값을 갖게 된다.

    return answer

# 참가자들의 이름의 hash값을 key로, 참가자의 이름은 value로 하는 딕셔녀리를 만들면서 temp라는 변수에 hash값들을 더해준다. 
# 그리고 완주자들의 이름을 for문을 돌리면서 완주자들의 이름의 해시값들을 temp에서 빼준다. 
# 이렇게 되면 temp는 오직 하나의 이름에 대한 해시값을 갖게 된다. 
# 앞서 만든 딕셔너리의 key는 이름의 해시값이므로 temp(비완주자 이름의 해시값)를 이용하여 비완주자를 찾을 수 있다. 
# 완주하지 못한 선수가 한명이라 가능한 방법같지만 hash함수를 잘 사용한게 신기했다.