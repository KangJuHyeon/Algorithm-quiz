def solution(s):
    answer = ''
    
    if (len(s) >= 1 and len(s) <= 5):
        answer = int(s)
        
    return answer

# 문자열 s를 숫자로 변환한 결과를 반환하는 함수
# 1보다는 크거나 같고, 5보다는 낮거나 같은 수
# 임의의 문자열이 들어오면, 그 문자열이 조건에 적합하다면 문자열의 값을 정수로 변환하여 할당하여 리턴한다.