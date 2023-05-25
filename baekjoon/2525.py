# 오븐 시계

hour, minute = map(int, input().split())
timer = int(input())

# print(hour, minute)

hour += timer // 60
minute += timer % 60

if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24

print(hour, minute)