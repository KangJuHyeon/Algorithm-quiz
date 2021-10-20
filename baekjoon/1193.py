# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

# 출력
# 첫째 줄에 분수를 출력한다.

X = int(input()) # X번째 분수의 입력 값
denominator = 0 # 분모
molecule = 0 # 분자

line = 1 # 사선 라인
while X > line: # 14 > 1
    X -= line
    line += 1

if line % 2 == 0: # 사선 라인이 짝수일 때
    denominator = X # 분모
    molecule = line - X + 1 # 분자
else: # 사선 라인이 홀수일 때
    denominator = line - X + 1 # 분모
    molecule = X # 분자
        
print(molecule, '/', denominator, sep='')
# print(f'{molecule}/{denominator}') 
# 27 line : 파이썬 리터럴을 사용했을 경우 통과 x