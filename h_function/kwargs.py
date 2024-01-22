# # keyword arguments
#
# def introduce(**intro): #딕셔너리
#     print(type(intro))
#     print(f'name : {intro["name"]}')
#
#
# introduce(name="이정륜") # 딕셔너리로 보내려면 위에서 **kwargs
# introduce(**{'name':'이정륜'}) # 딕셔너리를 통채로 보내려면 딕셔너리 앞에 **
#
#
# info_dict = {
#     'name':'이정륜'
# }
#
# # 주문 가격과 주문한 회원의 정보 출력
# def order_info(*args, **kwargs):
#     total = 0
#     for i in args:
#         total = total + i # 주문한 총 가격
#
#     print(f'{kwargs["name"]}님의 총 주문 가격 : {total}원')
#
# order_info(3000,20000, 1000, name = '이정륜')
#
#%%
# 국어 영어 수학 점수의 평균 구하기
# kwargs로 선언

def score_av(**kwargs):
    all = sum(kwargs.values())
    av = all/3
    return av

print(score_av(**{'kor':80 , 'eng':90 , 'math': 70}))
def score_av(**kwargs):
    kor = kwargs['kor']
    eng = kwargs['eng']
    math = kwargs['math']
    return (kor+eng+math)/3

print(score_av(kor=80,eng=90,math=70))
#
# 국어 영어 수학 점수의 평균 구하기
# 사용자가 원하는 자리수(round)에서 반올림해준다.
# 자리수를 받지 않았다면, 기본값을 리턴한다.
# 국어 영어 수학 점수의 평균 구하기
# kwargs로 선언

def average(**kwarg):
    if "round" in kwarg:
        kor, eng, math = kwarg.get('kor'), kwarg.get('eng'), kwarg.get('math')
        total = kor + eng + math
        ave = total/3
        if "round" in kwarg:
            return round(ave, kwarg['round'])
        return ave


print(average(kor=100, eng=30, math=22, round= 2))



# # 반드시 key와 함께 사용하고자 할 때에는 매개변수의 시작을 *로 한다.
# def average(*, kor, eng, math):
#     return kor + eng + math/3
#
# print(average(kor=100, eng=30, math=22)
# # 매개변수 앞에 *, 있다면 키 값을 매개변수에 입력

#%%
# 주문 총 가격과 주문한 회원의 정보 출력
def order_info(*args, **kwargs):
    '''
    주문 총 가격과 주문한 회원의 정보 출력
    :param args: 주문 가격들
    :param kwargs: 회원의 정보
    '''
    total = 0
    for i in args:
        total += i

    print(f'{kwargs["name"]}님의 총 주문 가격: {total}원')


help(order_info)