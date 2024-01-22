# for문으로 '🐼'를 이용하여 아래와 같은 도형을 만들기
'''
🐼
🐼🐼
🐼🐼🐼
🐼🐼🐼🐼
🐼🐼🐼🐼🐼
'''

for i in range(1,6):        # i를 1부터 5번 반복
  for j in range(i):        # j를 i만큼 반복 -> 따라서 판다가 줄마다 하나씩 늘어남
    print('🐼', end = '')  # end = '' 를 이용해 가로로 출력
  print()

#%%
# while문을 이용해 1부터 num까지 자연수 중 3의 배수의 합
num = int(input('숫자 입력: '))

result = 0
i = 1
while i <= num:                 # i 가 num에 도달하면 반복을 멈춤
    if i % 3 == 0:              # i가 3의 배수이면
        if result + i >= 10000: # 만약 result의 값이 10000을 넘으면
            break               # 반복문 종료
        result += i             # result에 3의 배수인 i를 더함
    i += 1                      # i 가 num에 도달하면 반복을 멈춤

print(result)                   # num까지 자연수 중 3의 배수의 합 결과

#%%
# if문으로 국영수 총합점수, 평균, 학점 구하기

kor, eng, math = input('국어 영어 수학').split('/') # 점수를 예) 90/80/70 입력
all = int(kor) + int(eng) + int(math)  # input에서 str로 입력된 값을 int로 변경 후 총합
av = all/3            # 평균

if av >= 90:
  grade = ('A')
elif av >= 80:
  grade = ('B')
elif av >= 70:
  grade = ('C')
elif av >= 60:
  grade = ('D')
else:
  grade = ('F')

print('총점: %d, 평균: %4.2f, 학점 %s' %(all, av, grade))

#%%
# 소괄호가 있으면 함수
# 함수앞에 .이 찍히면 앞은 클래스
