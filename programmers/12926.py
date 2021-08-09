# 문제 풀이
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식 => 시저 암호라고 한다.
# 문자열 s가 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수를 리턴하라. 
# 시저 암호를 적용한 함수를 리턴하라.

# 문제 접근
# 슬라이싱을 이용한 [::-1] 거리 간격?
# 소문자, 대문자, 공백 = s
# 리스트가 따로 있는 것인가? 알파벳을 어떻게 뒤로 새롭게 만들지? 뒤로 밀면 새롭게 생기는 것이 아니면 리스트가 있는 것인가?

# 수도코드
def solution(s, n):
    answer = ""
    result = len(s)
    for i in range(result):
        answer += result[n]+i
        # "AB" => "BC"가 되려면 어떻게? list가 있거나, 새롭게 만들어서 대체하거나인데...

# 문제풀이(1)
def solution(s, n):
    so = ','.join('abcdefghijklmnopqrstuvwxyz').split(',')
    dae = ','.join('ABCDEFGHIJKLMNOPQRSTUVWXYZ').split(',')
    s = ','.join(s).split(',')

    for i in range(len(s)):
        if s[i] in so: # 소문자일 경우
            if so.index(s[i]) + n <= 25:
                s[i] = so[so.index(s[i]) + n]
            else:
                s[i] = so[so.index(s[i]) + n - 26]
        
        elif s[i] in dae: # 대문자일 경우
            if dae.index(s[i]) + n <= 25:
                s[i] = dae[dae.index(s[i]) + n]
            else:
                s[i] = dae[dae.index(s[i]) + n - 26]
        
        else: # 공백일 경우
            continue 

    return "".join(s)

# 코드 해석
# line 21~23 : 소문자의 각 문자를 하나씩 so라는 리스트에 담고, 대문자의 각 문자를 하나씩 dae라는 리스트에 담는다. 이 후 입력값으로 받는 문자열 s 또한 각 문자를 하나씩 담는 리스트로 바꾼다.
# line 25 : 입력받은 문자열에 속한 모든 문자와 공백을 확인하기 위해 반복 횟수는 len(s)이다.
# line 27~30 : 만약 특정 문자가 소문자라면, 리스트 'so'에서 해당 문자가 몇 번째 index에 있는지 확인한다. 그 인덱스에 n칸을 오른쪽으로 미룬 값을 return해야 하니 '해당 인덱스+n'을 체크한다.
# '해당 인덱스 + n'이 리스트 'so'의 마지막 원소의 인덱스인 25이하라면 list index out of range 에러가 발생하지 않기 때문에 그대로 해당 문자를 오른쪽으로 n칸 미룬 값으로 바꿔준다.
# 반대로 '해당 인덱스 + n'이 25를 초과하게 된다면, 리스트 'so'의 처음으로 돌아간 다음 오른쪽으로 더 밀려가는 것으로 생각해야 한다. 
# 입출력 예시 3번을 보면 알기 쉬운데, 'z'가 오른쪽으로 4칸 밀려났을 때 list 범위를 초과해버리기 때문에 한 칸을 이동했을 때 리스트 'so'의 처음인 a로 돌아가게끔 처리해줘야 하며, 이 후 오른쪽으로 나머지 3칸을 더 이동하여 'd'가 된다.

# line 32~36 : 위에 내용과 똑같다. 대문자일 뿐 후후...
# line 38 : 공백일 경우에는 아무리 밀어도 공백이라는 제한 조건이 있으므로 무시하고 continue를 해준다.
# line 41 : 입력받은 문자열 s의 각 문자를 오른쪽으로 n칸 미룬 새로운 문자열은 현재 각 문자 하나하나로 떨어져있는 리스트 형태이다. 그렇기 때문에 "을 기준으로 합쳐준 문자열을 return 해준다.

# 문제풀이(2) 아스키 코드 사용
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper(): # 만약 대문자라면
            s[i] = chr((ord(s[i])-ord('A') + n) % 26 + ord('A'))
        elif s[i].islower(): # 만약 소문자라면
            s[i]=chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return "".join(s)

# Python ASCII
# ord(문자) : 문자에 해당하는 ASCII 정수값 반환 
# chr(정수) : 정수에 해당하는 ASCII 문자 반환
# string.ascii_lowercase : 소문자에 해당하는 ASCII 값 
# string.ascii_uppercase : 대문자에 해당하는 ASCII 값

# 문제풀이(2)
# 각 문자열을 하나씩 쪼개서 아스키 코드로 변환해야하기 때문에 list(s)로 치환해서 담는다.
# ord(s[i])-ord('A') (또는 ord('a')) 26으로 나눈 나머지 값에 'A'/'a' ASCII 값 = 97/65을 더해주면 n만큼 민 값이 나오게 된다.
# %26을 해주는 이유는? z 또는 Z의 범위를 넘어가지 않도록 하기 위해
# 즉, 맨 처음 값인 ord('A')와 ord('a')에서 n만큼 증가한 값이 무엇인지 찾는 것이다. 
# 아스키 코드를 사용하면 공백은 무시해도 된다.
# "A", "B" 이런식으로 입력값이 들어갈 것이기 때문에 마지막에 "".join 사용하여 붙여준다.