def solution(s):
    answer = True
    if (len(s) == 4 or len(s) == 6) & s.isdigit():
        return answer
    else: 
        return False

# 문자열인지 정수형인지 판별
# 예를 들어 s가 'a234'이면 False, '1234'라면 True 리턴
# def solution(s):
#   if (길이 4 or 6) and s.isdigit(): 
#       return True
#   else:
#       return False