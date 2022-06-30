# # 연습(1)
# import shapes.volume as vol

# # print(shapes.volume.cube(3))
# print(vol.cube(3))

# # 연습(2)
# from shapes.area import square

# print(square(3))

# # 연습(3)
# from shapes import volume

# print(volume.cube(3))

# # 연습(4)
# import shapes

# print(shapes.area.circle(2))
# print(shapes.volume.cube(2))

# # 연습(5) - init 파일
# import shapes
# import shapes.volume

# # 연습(6) - init import
# import shapes

# print(shapes.area.square(2))
# print(shapes.volume.cube(2))

# print(shapes.circle(2))
# print(shapes.square(2))

# # 연습(6) - __all__
from shapes import *
from shapes.area import *

print(dir())