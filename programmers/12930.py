def solution(s):
    result = s.split(' ')
    
    for i in range(len(result)):
        result2 = list(result[i])
        
        for j in range(len(result2)):
            if (j % 2 == 0):
                result2[j] = result2[j].upper()
            elif (j % 2 == 1):
                result2[j] = result2[j].lower()
        result[i] = ''.join(result2)
    
    answer = ' '.join(result)
            
    return answer

# 짝수일 때, 알파벳은 대문자로 변환하고, 홀수일 때, 알파벳은 소문자로 변환하라.
# "try", "hello", "world"를 어떻게 붙이지? 한 문장으로?
# 이 문제는 전체 문자열에 대한 인덱스 기준이 아니라 공백기준으로 잘라진 단어의 기준이다.
# 19번 째 줄 단어는 공백을 기준으로 짝/홀수 인덱스를 판단해야된다.
