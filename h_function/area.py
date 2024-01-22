# 전역 변수 (global variable) : 어떤 지역 밖에 선언된 변수
# 지역 변수 (local variable) : 어떤 지역 안에 선언된 변수
#                           => 여러 함수에서 공유해야하는 값이 있을 경우 사용

# def test():
#     data = 10 # 안에 선언되면 지역변수

#%%
count = 0 # 전역변수 : 밖에다가 변수선언

def increase():

    #지역변수
    #count = 0       # 밖에있는 전역변수와 다른 count이다.
    global count
    count += 1    # 전역변수를 수정하려면 global 키워드를 사용한다.

increase()
print(count)