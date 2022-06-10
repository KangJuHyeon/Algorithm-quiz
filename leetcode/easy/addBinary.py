class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = int(a, 2) + int(b, 2)

        return str(bin(answer)[2:])
print(Solution().addBinary("11", "1")) # "100"
print(type(Solution().addBinary("1010", "1011"))) # "10101"