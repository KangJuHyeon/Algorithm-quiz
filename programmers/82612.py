# 위클리 챌린지 1주차 문제 : 부족한 금액 계산하기
# 문제 풀이
# 만약 이용료(price)가 money보다 커지면 money를 뺀 값을 리턴한다.
# 매개변수로는 (price(이용료), money(금액), count(이용 횟수))가 있다.

# 나의 문제풀이(1)
def solution(price, money, count):
    answer = 0
    for i in range(1, count+1): 
        answer += price * i # 이용료는 한번 탈 때마다 올라감
        if answer >= money: # 만약 지금 가지고 있는 돈보다 이용료가 같거나 커진다면
            return answer - money # 이용료에서 지금 가지고 있는 값을 빼면 얼마가 모자란지 알 수 있다.
        else:
            return 0 # 금액이 부족하지 않은 경우

# 산술평균이란?
# 산술 평균(Arithmetic Mean)은 우리에게 가장 친숙한 평균입니다. '산술'을 생략하고 평균이라고도 사용됩니다. 
# '무도'반 수학 점수에 대한 산술 평균을 구한다고 해 봅시다.
# 익히 알고 있듯이 학생들의 점수를 다 더한 다음 학생수로 나눠 주면 평균, 즉 산술 평균을 구할 수 있습니다.
# 산술 평균 = 항목들을 다 더한 것 ÷ 항목들의 개수 무도반의 산술 평균 = 무도반 학생들의 점수를 다 더한 것 ÷ 무도반 학생 수 = (재석이 점수 + 명수 점수 + 홍철이 점수 + 형돈이 점수 + 하하 점수 + 준하 점수 + 태호 점수) ÷ 7명 = (99+62+34+87+75+84+91) ÷ 7 = 76

# 다른사람의 문제풀이(1) # 산술평균으로 풀이
def solution(price, money, count):
    return max(0, price * (count+1) * count // 2 - money) 
    # 3 * 5 * 4 // 2 - 20 = 10
    # 몫, 나머지의 값을 구하는 방법을 정확히 알아야 된다. 30 // 3 = 10(몫) 30 % 3 = 나머지는 0

# 다른사람의 문제풀이(2) # abs 함수를 이용한 풀이
def solution(price, money, count):
    return abs(min(money - sum([price * i for i in range(1, count+1)]), 0))

a = max(0, 3 * 5 * 4 // 2 - 20)
# price = 3
# money = 20
# count = 4
print(a)

# abs(x)란?
# 절대값을 구할때 abs라는 이름의 함수를 사용한다.
# 절대값을 구하고 싶은 수를 매개변수로 집어 넣고,
# 반환형으로 넣은 수의 절대값이 나온다.

# 매개변수로 넣은 숫자가 변하는 것이 아니라, 넣은 숫자는 가만히 있고,
# 넣은 숫자의 절대값이 반환되는 것이다.
# 매개변수로 넣은 숫자의 타입에 따라서 반환형의 타입이 달라진다.
# 정수를 넣으면 해당 정수의 절대값을 반환하고, 실수를 넣으면 해당 실수의 절대값이 반환된다.

# 1. 정수
num1 = -99
num2 = 99
print(f'abs({num1}) = {abs(num1)}') # abs(num1)
print(f'abs({num2}) = {abs(num2)}') # abs(num2)

# 2. 실수
num3 = -99.99
num4 = 99.99
print(f'abs({num3}) = {abs(num3)}') # abs(num1)
print(f'abs({num4}) = {abs(num4)}') # abs(num1)

# 3. 0의 절대값은? 0이겠죠?
num5 = 0
num6 = 0.0
print(f'abs({num5}) = {abs(num5)}') # abs(num1)
print(f'abs({num6}) = {abs(num6)}') # abs(num1)