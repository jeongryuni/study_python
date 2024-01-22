# 문자열 끼리만 연결(+)이 가능하다.
print('안'+'녕')
data = 3
print('안'+ str(data))

#%%
name = input("이름 : ") #입력보다 출력이 먼저됨
formatting = (f'{name}님 환영합니다.')
print(formatting)

#%%
#실습1)
# 제 이름은 ???, 키는 ???cm입니다.
name = input("이름 입력 : ")
height = input("키 입력 : ")
formatting = (f'제 이름은 {name}입니다. 키는 {height}cm입니다.')
print(formatting)
#%%
#실습2)
# 두 정수를 입력받은 후 곱셈 결과 출력
# num1 = int(input('첫번째 정수 입력 : '))
# num2 = int(input('두번째 정수 입력 : '))

num1, num2 = map(int,input('두 정수를 입력하세요').split(','))
total = num1 * num2
# map은 바꾸기 위해 사용
formatting = (f'{num1} * {num2} = {total}')
print(formatting)

#%%
a,b,c = 'A,B,C'.split(',')
print(a, b, c)

#%%
# map(각각 어떻게 바꿀 것인가, [바꿀 입력 값])
message = '두 정수를 입력하세요.'
example_mesaage = '예)1, 3'
num1,num2 = map(int, input(message + '\n' + example_mesaage + '\n').split(','))
result = num1 * num2
formatting = (f'{num1} * {num2} = {result}')

print(formatting)

#%%
# 실습
# 현재 시간을 입력하고 시와 분으로 분리하여 출력
# 핸드폰 번호를 -(하이픈)과 함꼐 입력받은 뒤 각 자리의 번호를 분리해서 출력
# 이름과 나이를 한 번에 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
# message1 = '현재 시를 입력하세요'
# message2 = '현재 분을 입력하세요'
# example_mesaage1 = '예)00시'
# example_mesaage2 = '예)00분'
#
# hour = input(message1 + '\n' + example_mesaage1 + '\n').split('시')
# minute = input(message2 + '\n' + example_mesaage2 + '\n').split('분')
# formatting = (f'{hour}시이고 ,{minute}분 입니다.')
# print(formatting)

# 현재 시간을 입력하고 시와 분으로 분리하여 출력
message = '현재 시간: '
time = input(message)
hours, minutes = time.split(':')
formatting = f'{hours}시 {minutes}분'
#
print(formatting)
#%%
# 핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
message = '핸드폰 번호: '
number1, number2, number3 = input(message).split('-')
formatting = f'통신사: {number1}\n앞번호: {number2}\n뒷번호: {number3}\n'

print(formatting)

#%%
# 이름과 나이를 한 번에 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
message = '이름과 나이를 입력하세요'
example_message = '예)홍길동 20'

name, age = input(message + '\n' + example_message + '\n').split()
formatting = (f'{name}님의 나이는 {age}살')
print(formatting)
#%%
# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
# 메세지 출력후 입력받은 값을 split으로 '/'로 분리
# 분리된 값이 각 변수에 저장
message = '3개의 정수를 입력해주세요'
example_message = '예)1/2/3'

num1,num2,num3 = map(int, input(message + '\n' + example_message + '\n').split('/'))
formatting = f'{num1} + {num2} + {num3} = {num1+num2+num3}'
print(formatting)

