# 문제풀이
# 다트 게임의 점수 계산 로직을 구현하면 된다.
# 문자열을 1제곱, 2제곱, 3제곱은 어떻게 계산하지?
# 조건식으로 하나씩 풀어보자.

# 문제풀이(1)
def solution(dartResult):
    answer = []
    pattern = ''
    for i in dartResult:
        # i가 숫자일 경우
        if i.isnumeric():
            pattern += i
            print(pattern)
        # i가 문자열 S와 같을 경우
        elif i == 'S':
            pattern = int(pattern) ** 1
            print(pattern)
            answer.append(pattern)
            print(answer)
            pattern = ''
        # i가 문자열 D와 같을 경우
        elif i == 'D':
            pattern = int(pattern) ** 2
            print(pattern)
            answer.append(pattern)
            print(answer)
            pattern = ''
        # i가 문자열 T와 같을 경우
        elif i == 'T':
            pattern = int(pattern) ** 3
            print(pattern)
            answer.append(pattern)
            print(answer)
            pattern = ''
        # i가 문자열 *와 같을 경우
        elif i == '*':
            # 만약 answer의 길이가 1보다 클 경우
            if len(answer) > 1:
                answer[-2] = answer[-2] * 2
                answer[-1] = answer[-1] * 2
            # 그렇지 않을 경우
            else:
                answer[-1] = answer[-1] * 2
        # i가 문자열 #와 같을 경우 
        elif i == '#':
            answer[-1] = answer[-1] * -1

    return sum(answer)
print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))


# 다른사람의 문제풀이(1)
# 내가 풀고싶은 정규표현식대로 잘 풀었다...(배우자)
import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer