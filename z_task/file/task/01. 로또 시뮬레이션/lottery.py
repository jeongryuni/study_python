import random

# 로또 시뮬레이션 프로그램: 번호뽑기
def generate_numbers(n):
    winner_numbers =[]
    while len(winner_numbers) < n:
        rand_num = random.randint(1, 45)
        if rand_num not in winner_numbers:
            winner_numbers.append(rand_num)
    return winner_numbers

# 로또 시뮬레이션 프로그램: 겹치는 번호 카운트
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    print(winning_numbers)
    sorted_winning_numbers = sorted(winning_numbers[0:6])
    # print(sorted_winning_numbers)
    bonus_number = winning_numbers[-1]

    return sorted_winning_numbers + [bonus_number]

# print(draw_winning_numbers())

# 로또 시뮬레이션 프로그램: 겹치는 번호 개수
def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for number in numbers:
        if number in winning_numbers:
            count = count + 1
    return count

# 테스트 코드
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))

# 로또 시뮬레이션 프로그램: 당첨 금액 확인
def check(numbers, winning_numbers):
    check_num = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_match = False
    for num in numbers:
        if num in winning_numbers[6:]:
            bonus_match = True
            break

    if check_num == 5 and bonus_match:
        result = '5000만원'
    elif check_num == 6:
        result = '10억원'
    elif check_num == 5:
        result = '100만원'
    elif check_num == 4:
        result = '5만원'
    elif check_num == 3:
        result = '5천원'
    return result

# 테스트 코드
# print(check([4, 12, 14, 28, 40, 41], [4, 12, 14, 28, 40, 41, 6]))
# print(check([4, 12, 14, 28, 40, 6], [4, 12, 14, 28, 40, 41, 6]))
# print(check([4, 12, 14, 28, 40, 44], [4, 12, 14, 28, 40, 41, 6]))
# print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))


# 로또 시뮬레이션 프로그램: 당첨금 확인
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 500000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

# 테스트 코드
# print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
# print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
