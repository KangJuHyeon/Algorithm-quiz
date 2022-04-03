# 문제풀이(1)
from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        answer = True
        stack = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
                print(stack)
            elif len(stack) != 0:
                if i == ")" and stack[-1] == "(" or i == "]" and stack[-1] == "[" or i == "}" and stack[-1] == "{":
                    stack.pop()
                    print(stack)
                else:
                    answer = False
                    print(answer)
                    break
            else:
                answer = False
                break
            
        if len(stack) != 0:
            answer = False
        
        return answer
print(Solution().isValid("()"))     # true
print(Solution().isValid("()[]{}")) # true
print(Solution().isValid("(]"))     # false

# 문제풀이(2)
from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        
        while True:
            if "()" in s:
                s = s.replace("()", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            else:
                return not s

print(Solution().isValid("()"))     # true
print(Solution().isValid("()[]{}")) # true
print(Solution().isValid("(]"))     # false