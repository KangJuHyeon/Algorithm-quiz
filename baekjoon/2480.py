# 주사위 세개

dice1, dice2, dice3 = map(int, input().split())

if dice1 == dice2 == dice3:
    print(10000 + dice1 * 1000)

elif dice1 == dice2:
    print(1000 + dice1 * 100)

elif dice1 == dice3:
    print(1000 + dice1 * 100)

elif dice2 == dice3:
    print(1000 + dice2 * 100)

else:
    print(100 * max(dice1, dice2, dice3))
