def solution(s):
    answer = ''
    result = s.split(' ')
    
    for word in result:
        for i in range(len(word)):
            if (i % 2 == 0):
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
            
    return answer[: -1]

# 짝수일 때, 알파벳은 대문자로 변환하고, 홀수일 때, 알파벳은 소문자로 변환하라.
# "try", "hello", "world"를 어떻게 붙이지? 한 문장으로?
# 이 문제는 전체 문자열에 대한 인덱스 기준이 아니라 공백기준으로 잘라진 단어의 기준이다.
# 19번 째 줄 단어는 공백을 기준으로 짝/홀수 인덱스를 판단해야된다.

# 문자열 s를 공백으로 분리하고, 변수에 담는다.
# for문을 사용해 변수 값을 순회(체크)하고, 새로운 문자열 길이 값을 담을 i를 선언하고
# 인덱스가 짝수면 대문자로 변환하고, 홀수면 소문자로 변환한다.
# 리스트에 마지막에 문자열로 '공백'을 넣어 기준을 잡는다.
# 마지막으로 리스트 마지막에 있는 배열을 제거해야되므로 슬라이싱을 이용해 제거해서 반환했다.
# 슬라이싱을 사용한 이유는 마지막에 공백 제거 함수를 사용해봤는데, 정확성 문제로 통과가 되질 않았다.