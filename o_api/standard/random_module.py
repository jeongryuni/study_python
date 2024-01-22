import random as r
print(r.randint(1, 10))


# randint(시작값, 끝값)
# 1~10까지 중 랜덤한 값 1개
# print(r.randint(1, 10))
#확률
#1. list 선언
단위 = 10
rating = [0] * 단위
확률 = 30

# 2. 확률을 계산해서 해당 자리에 1대입
for i in range(확률//10):
    rating[i] = 1

# 3. 10개중 1은 3개 있기 때문에, 1이 나올 확률은 30%이다.
if rating[r.randint(0, len(rating)-1)] == 1 : # 랜덤한 인덱스를 하나 뽑음
    print('강화성공')

#%%
import random as r

단위 = 10
단위_dict = {1:100, 10:10}
rating = [0] * 단위_dict[단위]
확률 = 30

for i in range(확률//10):
    rating[i] = 1

if rating[r.randint(0, len(rating)-1)] == 1 : # 랜덤한 인덱스를 하나 뽑음
    print('강화성공')
