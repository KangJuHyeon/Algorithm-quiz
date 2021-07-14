# 첫 번째 풀이
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
        result.append(phone_number[i])  

    return "".join(result)