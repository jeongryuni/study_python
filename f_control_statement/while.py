# 사용자가 입력한 정수가 몇 자리수인지 출력
# 1. 사용자에게 정수를 입력 받는다.
# 2. 입력받은 정수의 각 자리수를 센다.
# 3. 자리수를 출력한다.
# 힌트 몫과 나머지

count = 0
number = int(input('Enter a number: '))

while number > 0:
    number//= 10
    count += 1
print(count)
