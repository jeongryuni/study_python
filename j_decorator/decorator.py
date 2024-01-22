import datetime
# 텍스트파일 2번
def log_time(original_function):  # 데코레이터의 이름이 되는 함수
                                  # log_time에 원래 함수(original_function)를 받을 수 있게 준비해야함
                                  # log_time 데코레이터를 붙인함수가 original_function에 들어오게 됨
                                  # original_function을 사용했을때 전달한 값이
                                  # 클로저 함수(logging)의 매개변수 *args에 들어오게된다.
    def logging(*args):  # (클로저 생성) # 외부에서 args여러개를 받음 #log_time을 사용하면 args에 들어옴
        print('logging 들어옴')
        print(args)         # 매개변수 출력 확인
        print(datetime.datetime.now()) # 현재시간 출력
        print('logging 함수 종료')  # 출력
        return original_function(*args) # 위의 역할을 마친 후
                                        # original_function을 사용해서 *args를 그대로 전달

    print('log_time 함수 종료')
    return logging


@log_time
def add(*args):     # add함수를 사용하면 log_time함수 에 들어가게 된다. => log_time 사용
                    # 그리고 original_function에 add가 들어가면
                    # add에 전달한 값들 *args의 값은
                    # 그 안에 있는 클로저 logging함수의 매개변수(*args)에 받는다.
                    # 그리고 주변 로직이 실행된다 그리고 add함수가 사용되면서 결과값이
                    # return original_function(*args)리턴된다.

    total = 0
    for i in args:      # args값들을 더해주는 반복문
        total += 1
    return total        # 토탈값 리턴

result = add(1, 2, 3)
print(result)

# 출력 값 :
# log_time 함수 종료
# logging 들어옴
# (1, 2, 3)
# 2024-01-08 00:12:27.480940
# logging 함수 종료
# 3



# 로그타임이 사용된뒤
# 로깅이 사용
# 로그타임이 로깅을 리턴하기때문 -> 로그타임이 사용되어야 로깅을 사용할수 있다.
# 따라서 로그타임은 한번 사용이 된다.
# 그것을 이용해 로깅을 사용
# 매개변수 123을 받고
# add를 사용한 시간이 출력됨
# 로깅 종료
# 그리고나서 결과값이 리턴된다.

#%% # 내가만든 함수
# 평균을 구해주는 데코레이터를 제작한다.
# 여러 개의 정수를 전달받으면, 총 합을 직접 구해준 뒤 평균을 출력한다.
# 총 합(total)과 개수(count)를 전달받으면, 총 합/개수로 평균을 출력한다.
# 총 합을 구하는 함수를 제작한 뒤 데코레이터를 통해


# 총합을 구하는 함수 add처럼 따로 만듬
# 총합이 메인로직
# 평균이 주변로직
#   첫번째 상황은 args
#   두번째 상황은 kwargs, args
# 여러개 정수를 받으면 len != 0

'''
    2.
        def 데코레이터 이름(원래 함수):
            def 주변 로직 함수(원래 함수의 매개변수):
                주변 로직
                원래 함수(원래 함수의 매개변수)

            return 주변 로직 함수

            결과 :
평균 : 3.0
총 합: 15
평균 : 20.0
총 합: 100

'''
#
# def average(original_function):
#     def operate(*args, **kwargs):
#         count = len(args)
#         if count == 0:
#             total, count = kwargs['total'], kwargs['count']
#             result = total/count
#         else:
#             total = 0
#             for i in args:
#                 total += i
#                 result = total/count
#         print(f'평균 : {result}')
#
#         return original_function(*args,**kwargs)
#     return operate
# @average
# def set_datas(*args, **kwargs):
#     total = 0
#     for i in args:
#         total += i
#     print(f"총 합: {total if total != 0 else kwargs.get('total')}")
#
# # len이 0이면 총합과 개수를 전달받음 = > 나눠만 줌
# # 여러개 정수를 구했다면 직접 구해준뒤 평균 출력
#
# set_datas(1,2,3,4,5)
# set_datas(total = 100, count = 5)

#average(set_datas)(*args,**kwargs)
#
#
# #%%
# # import datetime
# #
# #
# # def log_time(original_function):
# #     print('log_time 들어옴')
# #
# #     def logging(*args):
# #         print('logging 들어옴')
# #         print(args)
# #         print(datetime.datetime.now())
# #         print('logging 함수 종료')
# #         return original_function(*args)
# #
# #     print('log_time 함수 종료')
# #     return logging
# #
# #
# # @log_time
# # def add(*args):
# #     total = 0
# #     for i in args:
# #         total += i
# #
# #     return total
# #
# #
# # result = add(1, 2, 3)
# # print(result)
#%%
# #
# 평균을 구해주는 데코레이터를 제작한다.
# 여러 개의 정수를 전달받으면, 총 합을 직접 구해준 뒤 평균을 출력한다.
# 총 합(total)과 개수(count)를 전달받으면, 총 합/개수로 평균을 출력한다.
# 총 합을 구하는 함수를 제작한 뒤 데코레이터를 통해 평균도 같이 확인할 수 있어야 한다.

# def average(original_function):
#     def operate(*args, **kwargs):                   #
#         count = len(args)
#         if count != 0:
#             total = 0
#             for i in args:
#                 total += i
#
#         else:
#             total = kwargs.get('total')
#             count = kwargs.get('count')
#
#         print(f"평균: {total / count}")
#
#         return original_function(*args, **kwargs)
#
#     return operate
#
#
# @average                                    # average 함수 데코레이저
# def set_datas(*args, **kwargs):             # 입력 값을 받아 위에 함수 operate로 넘김
#     total = 0
#     for i in args:
#         total += i
#     print(f"총 합: {total if total != 0 else kwargs.get('total')}")
#
#
# set_datas(1, 2, 3, 4, 5)
# set_datas(total=100, count=5)
