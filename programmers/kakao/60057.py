# s = "aabbaccc", return = 7
# "2a2ba3c" = 문자열길이 7
# s = "ababcdcdababcdcd", return = 9
# "2ababcdcd" = 문자열길이 9
# s = "abcabcdede", return = 8
# "2abcdede" = 문자열길이 8
# s = "abcabcabcabcdededededede", return = 14
# "2abcabc2dedede"
# s = "xababcdcdababcdcd", return =	17
# "x/ababcdcd/ababcdcd"

# 문제접근
# 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다? n만큼 슬라이싱해주세요.
# n만큼 자르고 그 문자열이 뒤로 붙는다. => "3ab"
# 자른문자열을 가지고 압축문자열을 만드는데 이 자른 단위들이 몇개가 있는지 어떻게 계산할까?
# 2번 예제 => "ababcdcdababcdcd" => 이걸 어떻게 2ababcdcd
# 4단위씩잘라서 2ababcdcd
# n개의 단위로 자른 문자열들을 모아서 그 중에서 가장 짧은 길이를 리턴하라

# 리스트 중복 요소 개수 찾기(카운팅)
def solution(s):
    answer = 0
    count = {}
    for i in s:
        try: count[i] += 1
        except: count[i] = 1
    # print(count)
    return count
print(solution("aabbaccc")) # {'a': 3, 'b': 2, 'c': 3}
print(solution("ababcdcdababcdcd")) # {'a': 4, 'b': 4, 'c': 4, 'd': 4}
print(solution("abcabcdede")) # {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2}
print(solution("abcabcabcabcdededededede")) # {'a': 4, 'b': 4, 'c': 4, 'd': 6, 'e': 6}
print(solution("xababcdcdababcdcd")) # {'x': 1, 'a': 4, 'b': 4, 'c': 4, 'd': 4}

# 문제풀이(1)
def solution(s):
    arr = [] # 자른 문자열들을 담는다. 제일 작은 문자열을 만들어야되니까

    # 테스트 케이스 5번 (s문자열 길이가 1일때)
    if len(s) == 1:
        return 1
        
    for n in range(1, len(s) // 2+1): # 문자열을 쪼갤 수 있는 최대 길이는 문자열 s의 반의 길이이다.
        print(n)
        answer = '' # 자른 문자열 넣어주기 위함
        count = 1 # 자른 단위들이 몇개가 있는지 확인(1이상)
        temp = s[:n] # 문자열을 쪼갠다 n만큼
        print(temp)
        for j in range(n, len(s)+n, n): # n만큼 잘라야되니까 n이 증가함으로써 n만큼 문자를 쪼갠다.
            print(j)
            if temp == s[j:j+n]: # temp의 문자열과 그 다음문자열이 같은지 비교
                count += 1 # 만약 같다면 카운트 1
                print(count)
            else: # 만약 비교했는데 아니라면?
                if count == 1: # count가 1과 같을때 빈 문자열에 쪼갠 문자열을 넣는다.
                    answer += temp
                    print(answer)
                else: # 만약 1과 같지 않을 때 빈 문자열에 'count' + 'temp(ab)'를 넣는다.
                    answer += str(count) + temp # '3' + 'aba' 이런식
                    print(answer)
                temp = s[j:j+n]
                print(temp)
                count = 1
        arr.append(len(answer))
        print(arr)
    return min(arr)
print(solution("aabbaccc")) # 7
print(solution("ababcdcdababcdcd")) # 9 
print(solution("abcabcdede")) # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd")) # 17