# 숫자 맞추기 게임

import random

secret_number = random.randint(1, 20)
count = 4

while count > 0:
    input_number = int(input("숫자입력: "))
    if input_number == secret_number:
        print(f"{count}번 만에 맞히셨습니다.")
        print("정답")
        break

    elif input_number != secret_number:
        count -= 1
        if input_number < secret_number:
            print(f"기회가 {count}번 남았습니다")
            print("up")
        else:
            print(f"기회가 {count}번 남았습니다")
            print("down")
    if count == 0:
        print(f"남은기회 {count}를 다 소모했습니다.")


#%%
import random

rand = random.randint(1, 20)
win = rand
print(win)

count = 0

while True:
    user = int(input("Enter your choice: "))

    if user == win:
        count+=1
        print(f"축하합니다 {count}번만에 숫자를 맞히셨습니다.")
        break

    elif user < win:
        count += 1
        print(f'기회가 {5 - count}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요 : {user}')
        print("Up")
        if count == 5:
            print(f"아쉽습니다. 정답은 {win}입니다.")
            break

    elif user > win:
        count += 1
        print(f'기회가 {5 - count}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요 : {user}')
        print("Down")
        if count == 5:
            print(f"아쉽습니다. 정답은 {win}였습니다.")
            break

