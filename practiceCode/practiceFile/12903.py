# 가운데 글자 가져오기(프로그래머스)

s = input()

if len(s) % 2 == 0:
    print(s[int(len(s) // 2 - 1) : int(len(s) // 2 + 1)])
else:
    print(s[int(len(s) // 2)])
    
print(8 // 2 -1)

# 8 / 2 - 1 = 3.5
# 8 / 2 + 1 = 4.5 
# "abcdefgh" => "de" 숫자 8이 들어가고, 4,5번째 숫자가 나오는 것을 보면 자동(기본) 올림 처리가 되어서 값이 나온다.