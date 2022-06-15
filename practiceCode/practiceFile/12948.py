# 핸드폰 번호 가리기(프로그래머스)

# s = input()
phone_number = ["01033334444", "0233338888"]
result = []

for i in range(len(phone_number) - 4): 
    result.append('*') # [*******]

for i in range(4): # i = 3 phone_number[10]
    result.append(phone_number[i + len(phone_number)- 4])  

print("".join(result))