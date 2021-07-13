def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        return s[int(len(s) / 2 - 1) : int(len(s) / 2 + 1)]
    else:
        return s[int(len(s) / 2)]
    return answer

# 단어의 길이가 짝수라면 가운데 두 글자를 반환하라.
# 5 / 2 - 1 = n
# 5 / 2 + 1 = n
# 7 / 2 - 1 = n
# 6 / 2 - 1 = 2.5
# 8 / 2 - 1 = 3.5
# 8 / 2 + 1 = 4.5 
# "abcdefgh" => "de" 숫자 8이 들어가고, 4,5번째 숫자가 나오는 것을 보면 자동(기본) 올림 처리가 되어서 값이 나온다.

# 한 줄 요약;
# return s[(len(str) - 1) // 2 : len(str) // 2 + 1]

# // 소수점 이하의 수를 모두 버리고 몫만 나타낼 때 ‘//’ 연산자를 사용한다.
# 그렇다면 8 / 2 - 1 = 3
# 8 / 2 + 1 = 4