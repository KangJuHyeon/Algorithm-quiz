# 첫번쨰 방법 find()
# find()함수는 찾고자하는 문자열이 존재하는 경우 시작 인덱스값을 리턴합니다.
# 찾는 문자열이 존재하지 않는 경우 -1을 리턴합니다.
# 그러므로 명확한 if문을 사용하여 조건 처리가 가능합니다.
x = "this is test string"
y = x.find("test")
print(y)

# 두번째 방법 in, not in
# 자주 사용하는 방법입니다. 결과 값이 존재하면 True를 리턴, 존재하지 않는다면 False를 리턴합니다.
# not in도 같습니다. 어떤 리스트에 "test"값이 존재하지 않는다면 False, 존재한다면 True를 리턴합니다.
x = "this is test string"
y = "test" in x

if y:
    print("찾는 문자열이 존재합니다.:", y)
else:
    print("찾는 문자열이 존재하지 않습니다.")

# 12919.py 서울에서 김서방 찾기 간단하게 연습해봤습니다.
# 입력 값 리스트에서 찾고자하는 문자열을 인덱스 값으로 추출해서,
# 그 result 리스트에 "Kim"의 문자열이 없다면 없다고 리턴하고,
# 있다면 김서방은 몇번째 인덱스에 있다고 나옵니다.
result = ["Jane", "Kim"]
x = result.index("Kim")
if "Kim" not in result:
    print(f"김서방은 {x}에 없다")
else:
    print(f"김서방은 {x}에 있다.")