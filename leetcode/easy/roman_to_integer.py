# 수도코드(1)
from typing import List
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900 }
        count = 0

        for i in s:
            for key, value in dict.items():
                print(key, value)
                if key == i:
                    count += value 
        # 앞뒤 비교해야 댐;
        return count
print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))

# 문제풀이(1)
from typing import List
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        count = 0

        for i in range(len(s)-1):
            first_num = dict[s[i]]
            # print(first_num)
            next_num = dict[s[i+1]]
            # print(next_num)
            if first_num >= next_num:
                count += first_num
            else:
                count -= first_num

        count += dict[s[len(s)-1]] # 1000 + 900 + 90 + 4
        # print(count)

        return count
print(Solution().romanToInt("MCMXCIV"))

# 문제풀이(2)
from typing import List
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900 }
        
        i = 0
        num = 0
        while i < len(s):
            # print(s[i:i+2])
            if i + 1 < len(s) and s[i:i+2] in dict:
                num += dict[s[i:i+2]]
                # print(dict[s[i:i+1]])
                # print(dict[s[i:i+2]])
                # print(num)
                i += 2
                # print(i)
            else:
                num += dict[s[i]]
                # print(num)
                i += 1
                # print(i)
        return num
print(Solution().romanToInt("MCMXCIV"))