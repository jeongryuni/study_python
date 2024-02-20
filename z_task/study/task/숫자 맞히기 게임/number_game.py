# 숫자 맞추기 게임
'''
실습 설명

1과 20 사이의 숫자를 맞히는 게임을 만들려고 합니다. random 모듈과 input() 함수를 활용하여 프로그램을 만들어 보세요.

진행 방식
1. 프로그램을 실행하면 기회가 *번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:가 출력됩니다.
    총 네 번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회가 줄어듭니다.

2. 정답을 맞히면 축하합니다. *번 만에 숫자를 맞히셨습니다.가 출력되고 프로그램은 종료됩니다.

3. 사용자가 입력한 수가 정답보다 작은 경우 Up이 출력되고, 입력한 수가 정답보다 큰 경우 Down이 출력됩니다.

4. 정답이 틀렸으면 1번부터 다시 진행합니다. 만약 네 번의 기회를 모두 사용했는데도 답을 맞히지 못했으면, 아쉽습니다.
    정답은 *입니다.가 출력되고 프로그램은 종료됩니다.

실습 결과
예시1)
기회가 4번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: 10
Up
기회가 3번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: 15
Up
기회가 2번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: 17
축하합니다. 3번만에 숫자를 맞히셨습니다.

예시2)
기회가 4번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: 19
Down
기회가 3번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: 14
Down
기회가 2번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: 6
Up
기회가 1번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: 10
UP
아쉽습니다. 정답은 12였습니다.
'''



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