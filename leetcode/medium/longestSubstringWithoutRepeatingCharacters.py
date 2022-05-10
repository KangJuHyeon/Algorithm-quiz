# 문제 해결 방법
# 한글자씩 비교 확인, 중복된 문자면 문자열을 자르고, 아니라면 뒤에 append
# 최대길이를 계속 저장, 비교

from typing import List

# 문제풀이(1)  
class Solution:
    def lengthOfLongestSubstring(self, s):
        string_box = []
        max_len = 0
        
        for i in s:
            if i in string_box: # 문자열이 중복된다면
                print(string_box[string_box.index(i):])
                print(string_box[string_box.index(i)+1:])
                string_box = string_box[string_box.index(i)+1:]
                print(string_box)
                
            string_box.append(i)    
            print(string_box)
            max_len = max(max_len, len(string_box))
            print(max_len)
            
        return max_len
print(Solution().lengthOfLongestSubstring("abcabcbb"))

# 문제풀이(2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 최대 길이인 문자열 길이를 리턴하면 된다.
        # 모든 길이의 경우를 담아야 한다.
        first_len = 0 # 처음 인덱스 초기값 0
        dic = {} # 객체로 담아서 { 0: a } 천천히 비교
        max_len = 0 # 최대 길이
        current_len = 0 # 현재 길이에서 최대 문자열 길이
        for key, value in enumerate(s):
            print(key, value)
            if value not in dic: # dic에 value값이 포함되어 잇지 않다면 현재 길이 +1, 처음 나오는 값이 여기로 들어옴
                dic[value] = key
                current_len += 1
            else: # 아니고, 같은 문자열이 들어온다면
                if dic[value] >= first_len:     # 현재 부분문자열 내에 중복되는 문자가 포함
                    first_len = dic[value] + 1  # 시작 인덱스 변경
                    current_len = key - dic[value]   # 변경된 현재 길이
                    dic[value] = key      # 중복된 문자의 마지막 위치 인덱스 갱신
                else:   # 현재 부분문자열 내에 포함되지 않아 영향이 없을 때
                    dic[value] = key
                    current_len += 1
            
            if current_len > max_len:
                max_len = current_len
        
        return max_len
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))