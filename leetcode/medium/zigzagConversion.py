from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = []
        obj = {}
        idx = 0
        down = 1
        up = -1
        joystick = 0
        for i in s:
            print(i)
            if idx == 0:
                joystick = down
                print(joystick)
            elif idx == numRows - 1:
                joystick = up
                print(joystick)
            obj[idx] = obj.get(idx, '') + i
            print(obj[idx])
            idx += joystick
            print(idx)
        print(obj)
        return ''.join(obj.values())
print(Solution().convert("PAYPALISHIRING", 3))
print(Solution().convert("PAYPALISHIRING", 4))