# 여러 개의 변수를 한 줄에 선언
a = 10; b = 20; c = 30
print(a, b, c, sep=', ')

a, b, c = 100, 200, 300
print(a, b, c)

# 변수의 값을 서로 바꾸기
a = 11
b = 33
print(a, b)

# temp = a
# a = b
# b = temp
# print(a, b)

a, b = b, a
print(a, b)

# 동적 바인딩
a = 10
print(type(a))

a = 10.5
print(type(a))

a = 'A'
print(type(a))

a = "ABC"
print(type(a))

a = ['A', 'B', 'C']
print(type(a))

a = {'A': 1, 'B': 2, 'C': 3}
print(type(a))

a = True
print(type(a))

# 변수명 주의사항
age = 10
print(type(age))

num = 10.5
print(type(num))

score = 'A'
print(type(score))

data = "ABC"
print(type(data))

course = ['A', 'B', 'C']
print(type(course))

level = {'A': 1, 'B': 2, 'C': 3}
print(type(level))

condition = True
print(type(condition))


# 서식문자
# 5의 경우에는 5의 앞자리가 홀수인 경우에 올림을 하고, 짝수인 경우에 버림을 하여 짝수로 만들어준다.
# 예를 들어 53.45는 53.4로, 32.75는 32.8로 반올림한다.
# 이를 오사오입(round-to-nearest-even)이라고 한다.

name = '이정륜'
age = 25
height = 157.45

print("이름 : %s" % name)
print("이름 : %s" % '푸바오')
print("나이 : %d" % age)
print("키 : %.2f" % height)

print("이름 : %s\n나이 : %d살\n 키 : %.2f" %(name, age, height))

### 실습(숙제)
### 정수 2개를 변수에 담기
### 두 정수의 합을 아래 형식으로 출력하기
### 1 + 3 = 4

# format 함수
name = '이정륜'
age = 25
height = 158.34

print('이름 : {}\n나이 : {}\n키 : {:.1f}'.format(name, age, height))
print('이름 : {0}\n나이 : {1}\n키 : {2:.1f}'.format(name, age, height)) # list
print('이름 : {name}\n나이 : {age}\n키 : {height:.1f}'.format(name=name, age=age, height=height)) #dict

formatting1 = '이름 : {}\n나이 : {}\n키 : {:.1f}'.format(name, age, height)
formatting2 = '이름 : {0}\n나이 : {1}\n키 : {2:.1f}'.format(name, age, height)
formatting3 = '이름 : {name}\n나이 : {age}\n키 : {height:.1f}'.format(name=name, age=age, height=height)

print('=' * 20)
print(formatting1)
print('=' * 20)
print(formatting2)
print('=' * 20)
print(formatting3)
print('=' * 20)
# format string
print(f'이름 : {name}')


# 실습
# 아래 메시지를 foramt함수를 사용하여 출력한다.
# Hello 파이썬, Python is fantastic!
# Hello 장고, Django is fantastic!
# Hello 리액트, React is fantastic!

# format string
print('=' * 20)
name = '이정륜'
age = 20
height = 156.26

print(f'이름 : {name}')
print(f'나이 : {age}살')
print(f'키 : {round(height, 1)}')




# 실습(숙제) 1-1)
# 정수 2개를 변수에 담기
# 두 정수의 합을 아래 형식으로 출력하기
# 1 + 3 = 4

num1 = 11
num2 = 22
total = num1 + num2
foramtting = '%d + %d = %d' %(num1, num2, total)
print(foramtting)


# 실습 2-1)
# 아래 메시지를 foramt함수를 사용하여 출력한다.
# Hello 파이썬, Python is fantastic!
# Hello 장고, Django is fantastic!
# Hello 리액트, React is fantastic!

python_kor, python_eng = '파이썬', 'Python'
django_kor, django_eng = '장고', 'Django'
react_kor, react_eng = '리액트', 'React'

# 자동으로 해당 순서에 값 부여
python_formatting = 'Hello {}, {} is fantastic!'.format(python_kor, python_eng)
# 값에 할당된 번호를 작성하면 해당 값 반영
django_formatting = 'Hello {0}, {1} is fantastic!'.format(django_kor, django_eng)
# 값에 이름을 붙이면 해당 이름에 값이 반영
react_formatting = 'Hello {kor}, {eng} is fantastic!'.format(kor = react_kor, eng = react_eng)

print(python_formatting, django_formatting, react_formatting, sep='\n')

# 실습 2-2)
# 아래 메세지를 format함수를 사용하여 출력한다.
# Hello 파이썬, Python is fantastic !
# Hello 장고, Django is fantastic !
# Hello 리액트, React is fantastic !

python_kor, python_eng = '파이썬', 'Python'
django_kor, django_eng = '장고', 'Django'
react_kor, react_eng = '리액트', 'React'

python_formatting = f'Hello {python_kor}, {python_eng} is fantastic !'
django_formatting = f'Hello {django_kor}, {django_eng} is fantastic !'
react_formatting = f'Hello {react_kor}, {react_eng} is fantastic !'

print(python_formatting, django_formatting, react_formatting, sep='\n')

