from random import randint

# 숫자 야구: 숫자 3개 뽑기
def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        number = randint(0, 9)
        if number not in numbers:
            numbers.append(number)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

# 테스트 코드
# print(generate_numbers())

# 숫자 야구: 숫자 예측하기
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        try:
            user_input = int(input(f'{len(new_guess) + 1}번째 숫자를 입력하세요.'))
            if user_input not in new_guess:
                if 0 <= user_input < 10:
                    new_guess.append(user_input)
                elif user_input > 10:
                    print('범위를 벗어나는 숫자입니다 다시 입력해주세요.')
            else:
                print('중복되는 숫자입니다. 다시 입력하세요.')

        except ValueError:
                print('숫자만 입력해주세요')
    return new_guess

# 테스트 코드
# print(take_guess())

# 숫자 야구: 점수 계산
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(len(solution)):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] != solution[i] and guesses[i] in solution:
            ball_count += 1

    return f'{strike_count}S, {ball_count}B'


# 테스트 코드
# s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
# print(s_1, b_1)
#
# s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
# print(s_2, b_2)
#
# s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
# print(s_3, b_3)
#
# s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
# print(s_4, b_4)

# 여기서부터 게임 시작!
tries = 0
ANSWER = generate_numbers()
while True:
    USER = take_guess()
    SCORE = get_score(ANSWER, USER)

    if USER != ANSWER:
        tries += 1
        print(f'시도 횟수 : {tries}\n{SCORE}\n')

    elif USER == ANSWER:
        tries += 1
        print(f'{SCORE}\n{tries}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.')
        break
