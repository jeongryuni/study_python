# 회원의 주문금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.
#%%
def get_total(*args, **kwargs):
    count = kwargs['count'] #쿠폰개수 -> 3
    coupon = kwargs['coupon'] * 0.01 #쿠폰 할인율 -> 40 * 0.01
    coupon_list = [coupon] * count  # [0.4] * 쿠폰개수 4
    user_price = [] # args를 반복하여 user_price에 주문금액을 넣음
    result = []

    for i in args:              # 주문금액을 뽑기 위한 반복문
        user_price.append(i)

        # 쿠폰이 주문금액보다 많거나 같을때
    if len(user_price) <= len(coupon_list) :    # 만약 user_price가 쿠폰개수보다 작거나 같으면
        for i in range(len(user_price)):        # user_price의 개수3 range(3)만큼 반복
            result.append(int(user_price[i])-int((user_price[i]) * coupon)) # 주문금액[i]-(주문금액[i] * 할인율)
                                                                            # 소수점을 없애기 위해 int
        return result
        # 쿠폰이 주문 금액보다 적거나 같을때
    else:
        if len(user_price) >= len(coupon_list): # 만약 주문금액이 쿠폰리스트보다 크거나 같으면
            for i in range(len(coupon_list)): # (주문금액 길이 - 쿠폰할인율 개수)만큼 반복 => 3-1 =>range(2)
                user_price[i] = int(user_price[i])-int((user_price[i]) * coupon) # 주문금액[i] - (주문금액[i] * 할인율)
        return user_price

print(get_total(1000,4000,5000, count = 2, coupon = 40))  # 쿠폰의 개수에 따라 앞부터 할인 가격 출력


#%%
# 컴프리헨션
def get_total(*args, **kwargs):
    coupon = kwargs['coupon']
    count=kwargs['count']

    return[(args[i] * (100 - coupon))// 100 for i in range(len(args)) if i < count]
    # 주문금액(range(args))을 반복을 돌려 개수를 i만큼 뽑아 args[i]에 반복문을 부여
    # if문이 True일때 만약 주문금액의 개수(i(args))가 쿠폰의 개수보다 작거나 같다면
    # if문 앞 실행 => (주문금액 * 100-할인율)//100 연산
    # if문이 False일때 args[i] 주문금액이 그대로 출력


print(get_total(1000,4000,5000, count = 4, coupon = 40))

#%%
# def get_total(*args, **kwargs):
#
#
#     result = []
#
#     for i in range(kwargs['count']): # 쿠폰의 개수 만큼 반복문 실행 i=0 ...i=4
#         if len(args) >= i + 1 : # 주문횟수가 쿠폰의 개수보다 많다면 / 쿠폰i=1 ...i=5까지
#             pay = int(args[i] - (args[i] * (0.01 * kwargs['coupon']))) # 주문금액[i] - ((주문금액[i] * (쿠폰할인율))
#             result.append(pay)
#     return result
#
#
#
#
#
#
# print(get_total(1000,4000,5000, count = 3, coupon = 40))

#%% 선생님 풀이
#[700,2800,3500]

# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.

# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시2
# [700, 2800, 3500]
#%%
def use_coupon(*pay, **kwargs):
    '''

    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''
    if 'coupon' in kwargs:      # 만약 kwargs 안에 쿠폰이 있다면
        return [
            int((1 - kwargs.get('coupon') * 0.01) * pay[i])
            for i in range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
        ]
        # if kwargs.get('count') <= len(pay) : 만약 쿠폰의 개수가 주문 금방보다 작거나 같으면
        # 쿠폰 개수만큼 반복을 하고
        # # True : ( (1 - 할인율 * 0.01) * 주문 금액 ) 를 실행한다.
        # 아니면 주문금액을 그대로 출력
    return None


help(use_coupon)
result = use_coupon(1000, 2000, 3000, coupon=50, count=2)

if result:
    print(result)
else:
    print('쿠폰이 없습니다.')

