# 첫 번째 풀이 (프로그래머스 기준 통과가 안됨)
def solution(phone_number):
    
    for i in range(len(phone_number) - 4):
        phone_number = phone_number.replace(phone_number[i], "*")

    return phone_number

# 두 번째 풀이
def solution(phone_number):
    answer = ''
    number = len(phone_number)
    answer = "*" * (number - 4)
    answer += phone_number[-4:]
        
    return answer

# 세 번째 풀이
def solution(phone_number): # 010 3333 4444
    result = []
    
    for i in range(len(phone_number)-4): 
        result.append('*') # [*******]

    for i in range(4): # i = 3 phone_number[10]
        result.append(phone_number[i + len(phone_number) - 4])  

    return "".join(result)


# 슬라이싱으로 맨 뒤 문자열을 자르고, 나머지 숫자들을 *을 출력
# ['*' : (len(phone_number) - 4)]

# for문으로 문자열 길이에서 -4를 뺸 값을 리스트에 담는다.
# for문으로 문자열 길이를 뺸 값에서 '*'로 모두 바꿔 리스트에 담고, 이어 붙여서 반환한다.

# for문을 사용할 필요없이 phone_number의 길이를 변수에 담고, 
# '*'와 길이를 담은 변수를 곱하여 변수에 담는다. ('*' * 7)
# 그 변수를 담은 값과 phone_number[-4:] 리스트에 뒤에 값부터 4개의 수를 슬라이싱해준다.

# 1. 전화번호 길이를 구하고, 뒷 자리 4개를 빼고는 변환할 것이니, 전화번호 길이 -4 의 값 만큼 *으로 변환해준다.
# 2. 그 다음 전화번호 뒷 자리 4자리를 -4 인덱스를 활용하여 잘라 붙이면 답이 나온다.
