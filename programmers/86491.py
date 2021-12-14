# 위클리 챌린지(1단계) : 최소직사각형

# 문제읽기
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들어라.
# 80 x 70 = (5600), 80 x 50 = (4000)

# 문제 접근
# 가로에선 80(max)값인데, 세로길이는 50(max)값이 아님.
# 모든 명함을 담을 수 있는 가장 작은 크기의 명함케이스를 구해야한다.
# 다시, 배열안에 있는 크기들을 제일 큰 값으로 정렬하고, 1번째 인덱스에 있는 수 중에도 제일 큰 값을 구해 곱하면 해결.
# max, min은 문자열로 변환했을 때 가능해서, 그 부분에서 시간을 많이 잡아먹었다.
# max, min = iterable, iterable 자료형이란? 문자열, 리스트, 튜플 등이 있다.

# 수도코드(1)
def solution(sizes):
    answer = 0
    sizes = [sorted(size, reverse=True) for size in sizes]
    print(sizes)
    for size in sizes:
        widths = [size[0]]
        # print(widths)
        heights = [size[1]]
        # print(heights)
        width, height = max(widths), max(heights)
        print(widths, heights)
        # answer = width * height
    return answer
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
# print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
# print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

# 문제풀이(1)
def solution(sizes):
    w, h = 0, 0

    for wh in sizes:
        if w < max(wh):
            w = max(wh)
            
        if h < min(wh):
            h = min(wh)
    return w * h
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

# 다른사람의 문제풀이(1)
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

# 다른사람의 문제풀이(2)
def solution(sizes): 
    answer = 0 
    sizes = [sorted(size, reverse=True) for size in sizes] 
    
    widths = [size[0] for size in sizes] 
    heights = [size[1] for size in sizes] 

    width, height = max(widths), max(heights) 
    answer = width * height 
    
    return answer
