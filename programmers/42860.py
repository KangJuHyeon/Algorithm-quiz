# 문제접근
# 알파벳 순서를 선언하고 그 선언한 문자열, 배열에서 알파벳 이동의 최솟값을 구한다.
# 키패드와 같이 오른쪽 왼쪽 중에 어떤 문자가 더 가까이 위치한지 알아야한다.

# 문제풀이
# 모든 target 문자에 대해 A로부터의 거리와 Z로부터의 거리 중 작은 값 저장( target문자 A일 경우 변환 필요없으므로 값 0 넣어줌)
# left, right 각각 1씩 늘려가며 target 문자 A가 아닌 문자에 먼저 도달하는 경우 찾기.
# left, right 중 더 짧은 거리의 위치로 이동하여 반복

# 문제풀이(1)
def solution(name):
    answer = 0 # 조이스틱 조작 횟수의 최솟값을 담아 리턴한다.
    pos = 0 
    alpha = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
    
    while True:
        answer += alpha[pos]
        print(answer)
        alpha[pos] = 0
        print(alpha[pos])

        if sum(alpha) == 0: break

        right = 1
        left = 1
        print(right)
        print(left)

        while alpha[pos - left] == 0:
            left += 1

        while alpha[pos + right] == 0:
            right += 1

        if right <= left:
            pos += right
            answer += right
        else:
            pos -= left
            answer += left
    
    return answer
print(solution('JEROEN')) # 56
print(solution('JAN')) # 23

# 문제풀이(2)
def solution(name):
    name = list(name)
    answer = 0
    i = 0
    print(name)
    
    while True:
        answer += min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
        name[i] = 'A'
        print(answer)
        
        if name.count('A') == len(name) : return answer
        
        left = 1
        right = 1
        for l in range(1,len(name)):
            if name[i-l] == 'A': 
                left += 1
            else: 
                break
        
        for r in range(1,len(name)):
            if name[i+r] == 'A': 
                right += 1
            else: 
                break
        
        if left < right:
            answer += left
            i -= left
        else:
            answer += right
            i += right
            
    return answer
print(solution('JEROEN')) # 56