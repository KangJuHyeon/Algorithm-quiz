# 문제
# 월드전자는 노트북을 제조하고 판매하는 회사이다. 노트북 판매 대수에 상관없이 매년 임대료, 재산세, 보험료, 급여 등 A만원의 고정 비용이 들며, 한 대의 노트북을 생산하는 데에는 재료비와 인건비 등 총 B만원의 가변 비용이 든다고 한다.
# 예를 들어 A=1,000, B=70이라고 하자. 이 경우 노트북을 한 대 생산하는 데는 총 1,070만원이 들며, 열 대 생산하는 데는 총 1,700만원이 든다.
# 노트북 가격이 C만원으로 책정되었다고 한다. 일반적으로 생산 대수를 늘려 가다 보면 어느 순간 총 수입(판매비용)이 총 비용(=고정비용+가변비용)보다 많아지게 된다. 최초로 총 수입이 총 비용보다 많아져 이익이 발생하는 지점을 손익분기점(BREAK-EVEN POINT)이라고 한다.
# A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 21억 이하의 자연수이다.

# 출력
# 첫 번째 줄에 손익분기점 즉 최초로 이익이 발생하는 판매량을 출력한다. 손익분기점이 존재하지 않으면 -1을 출력한다.

# 임대료, 재산세, 보험료, 급여 = A만원 고정 비용
# 한 대의 노트북을 생산하는 데에는 재료비와 인건비 = B만원 가변 비용

# 회계학
# 손익분기점 계산법 : TC = FC + VC
# TC(총 영업비용) = FC(고정영업비용)+ VC(변동영업비)
# Q(매출량) = 고정영업비용 / (판매가격-단위당 변동비) = A / C-B = 
# TR(매출액) = 판매가격 * Q

# 총 수입 = 고정비용 + 가변비용

# 문제 풀이(1)
A, B, C = map(int, input().split())
if B >= C: # 판매가격보다 변동비가 더 높아지면 손익분기점이 생길수가없다.
    print(-1)
else:
    print(int(A//(C-B)+1))

# 문제 풀이(2) 런타임에러남;
A, B, C = map(int, input().split())

Q = A / (C-B) # 매출량
# print(int(Q)+1)
TR = C * Q # 매출액
# print(int(TR))
if B >= C:
    print(-1)
else:
    print(int(Q+1))