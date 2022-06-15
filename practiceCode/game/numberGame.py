# 문제 풀이(1)
import random
result = random.randrange(1, 20)
# print(result)

# 코드를 작성하세요.
for i in reversed(range(1, 5)):
    chance = int(input(f"기회가 {i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))

    if chance == result:
        print(f"축하합니다. {i}번 만에 숫자를 맞히셨습니다.")
    elif chance < result:
        print("Up")
    elif chance > result:
        print("Down")

print(f"아쉽습니다. 정답은 {result}입니다.")
    
# 문제 풀이(2)
import random

# 상수 정의
ANSWER = random.randint(1, 20)
NUM_TRIES = 4

# 변수 정의
guess = -1
tries = 0

while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(NUM_TRIES - tries)))
    tries += 1    
    
    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")

if guess == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))