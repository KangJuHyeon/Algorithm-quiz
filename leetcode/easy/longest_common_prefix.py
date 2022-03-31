from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        print(strs)
        shortest = strs[0]
        print(shortest)
        prefix = ''
        for i in range(len(shortest)):
            print(strs[len(strs) - 1][i])
            print(shortest[i])
            if strs[len(strs) - 1][i] == shortest[i]:
                prefix += strs[len(strs) - 1][i]
                print(prefix)
            else:
                break
            
        return prefix
print(Solution().longestCommonPrefix(["flower","flow","flight"]))

def get_prefix(string):
  if len(string) == 0:
    return ''
    
  string.sort() # 정렬해주기
  shortest = string[0] #비교 기준이 되는 문자열 뽑기
  prefix = '' # 여기다가 넣어줄거야
  
  for i in range(len(shortest)): 
    if string[len(string)-1][i] == shortest[i]: 
      prefix += string[len(string)-1][i]
    else:
      break
      
  return prefix