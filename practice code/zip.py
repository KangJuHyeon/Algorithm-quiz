# zip 함수 연습하기 1차배열
arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [6, 5, 4, 3, 2, 1]
print([a + b for a, b in zip(arr1, arr2)])
# [7, 7, 7, 7, 7, 7]

# 2차배열
arr1 = [[1, 2, 3], [4, 5, 6]]
arr2 = [[6, 5, 4], [3, 2, 1]]
print([[x + y for x, y in zip(a, b)] for a, b in zip(arr1, arr2)])
# [[7, 7, 7], [7, 7, 7]]