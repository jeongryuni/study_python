#%%
# 1~ 15까지 출력
for i in range(1, 16):
    print(i)
#%%
# 30 ~ 1까지 출력
for i in range(30):
    print(30 - i)
#%%
# 1에서 100까지 중 홀수만 출력
# for i in range(1, 100):
#     if i % 2 == 1:
#         print(i)
# 반복횟수를 죽여야함
#
for i in range(50):
    print(i * 2 + 1, end=' ')
#%%
# 1~10까지 합 합 출력
sum=0
for i in range(0, 10):
    sum += i + 1
print(sum)
#%%
# 1~n까지 합 출력
num = int(input('정수를 입력하세요 : '))

sum=0

for i in range(1, num+1):
    sum += i
print(sum)
#%%
# 3 4 5 6 3 4 5 6 3 4 5 6 출력
for i in range(12):
    print( i % 4 + 3 , end= ' ')
#%%
# '1,235,500'를 1235500으로 출력
data = '1,235,500'
result = ''
for i in data:
    if i != ',':
        result += i

result = int(result)
print(result + 5)

#%%
# 1~10 까지 중 3까지만 출력
# print를 break아래에 작성하면
# i가 2일때 멈춰버려서 3이 출력되지 않음
for i in range(10):
    print(i+1)
    if i == 2:
        break
#%%
# 1~10까지 중 4를 제외하고 출력
for i in range(10):
    if i == 3:
        continue
    print(i+1)
# continue를 사용한다는건 밑에 코드를 사용하지 않기 위해 사용
# 따라서 continue를 만나면 다음 줄은 출력되지 않음
# 그러므로 print(i+1)을 continue 아래에 작성해야 i==3일때 print(i+1)을 출력하지 않고 넘어감

