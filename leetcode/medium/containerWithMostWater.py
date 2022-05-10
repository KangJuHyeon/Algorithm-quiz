# 정사각형 넓이: 가로 x 세로

# 연습코드(1)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        answer = []
        for i in range(len(height) - 1):
            for j in range(i+1, len(height)):
                spareHeight = min(height[i], height[j]) # 두 개의 높이 값 중 작은 것을 선택해야 물이 넘치지 않는다.
                spareWidth = abs(i-j) # 음수가 나오지 않게 abs 절대값으로 처리함
                result = spareHeight * spareWidth
                answer.append(result)
                print("i가 {}, j가 {}, spareHeight가 {}, spareWidth가 {}, result가 {}".format(i, j, spareHeight, spareWidth, result))
        answer.sort()
        return max(answer)
print(Solution().maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(Solution().maxArea([1,1])) # 1

# 연습코드(2)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max = 0
        length = len(height)
        
        # 오른쪽 기둥이 왼쪽으로 갈 때, 제일 높은 기둥을 채택한다.
        # 왼쪽 기둥에서 for start
        for i in range(0, length-1):
            # print("i", i)
            spareHeigth = height[i] # 왼쪽 기둥의 높이
            spareWidth = 0 # 오른쪽에 더 높은 기둥이 없을 때
            # 오른쪽 기둥에서 for start, -1 step 찾는다.
            for j in range(length-1, i, -1):
                print("i는 {}, j는 {}".format(i, j))
                # 오른쪽 기둥의 높이가 크거나 같다면 넓이 계산
                if spareHeigth <= height[j]:
                    spareWidth = j - i
                    # print("spareWidth", spareWidth)
                    break

            if max < spareWidth * spareHeigth:
                max = spareWidth * spareHeigth
                print("spareWidth는 {}, spareHeigth는 {}, max는 {}".format(spareWidth, spareHeigth, max))
        
        # 왼쪽 기둥이 오른쪽으로 갈 때, 제일 높은 기둥을 채택한다.
        for i in range(length-1, 0, -1):
            spareHeigth = height[i]
            spareWidth = 0
            for j in range(0, i):
                print("i는 {}, j는 {}, spareWidth는 {}, spareHeigth는 {}".format(i, j, spareWidth, spareHeigth))
                if spareHeigth < height[j]:
                    spareWidth = i - j
                    break
            if max < spareWidth * spareHeigth:
                max = spareWidth * spareHeigth
                print("spareWidth는 {}, spareHeigth는 {}, max는 {}".format(spareWidth, spareHeigth, max))
                # print("max2", max)
        
        return max
print(Solution().maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(Solution().maxArea([1,1])) # 1

# 연습코드(3) ::: 브루스포스, 시간복잡도 n^2
class Solution:
    def maxArea(self, height: list[int]) -> int:
        answer = set()
        for i in range(len(height) - 1):
            for j in range(i+1, len(height)):
                # 빗물이 넘치면 안되니까 서로 다를 때, 제일 큰 넓이를 구하는 게 핵심;
                if i != j:
                    result = min(height[i], height[j])
                    width = j - i
                    answer.add(result * width)
                    # answer.append(result * width)
                    # answer.sort()
                    print("i가 {}, j가 {}, result가 {}, answer가 {}".format(i, j, result, answer))
        return max(answer)
print(Solution().maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(Solution().maxArea([1,1])) # 1

# 문제풀이(1) ::: 시간복잡도 n, 브루스 포스에 비해 훨씬 빠르다. => 투 포인터
class Solution:
    def maxArea(self, height: list[int]) -> int:
        answer = set()
        l = 0
        r = len(height) - 1
        while l != r:
            if height[l] <= height[r]:
                h = min(height[l], height[r])
                w = r-l
                answer.add(h*w)
                l += 1
            else:
                h = min(height[l], height[r])
                w = r - l
                answer.add(h*w)
                r -= 1
        return max(list(answer))
print(Solution().maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(Solution().maxArea([1,1])) # 1