# # # f(x) = 2x+1
# # def f(x):
# #     return 2 * x + 1
# #
# # result = f(2)
# # print(result)
# from g_collection.dict.task.dict_task import keyword
#
#
# # 두 정수의 곱셈 함수
# def multiple(num1, num2):
#     return num1 * num2
# #%%
# #두 정수의 나눗셈 후 몫과 나머지 구하는 함수
# def divide(num1, num2):
#     if num2 != 0:
#         return num1 / num2, num1 % num2
#     return None
#
# #리턴이 2개인 이유
# #함수값이 리턴값에 맞다면 첫번째 리턴에서 끝이나고
# #첫번째 리턴값이 틀리다면 두번째 리턴
# #목적에 맞게 print문을 써야함
# #%%
# #1~10까지 print()로 출력하는 함수
# def print_ten(num):
#     for i in range(num):
#         print(i)
#
# print_ten(11)
# #%%
# # 이름을 n번 print()로 출력하는 함수
# def name_ten(name):
#     for i in range(10):
#         print(name)
#
# name_ten('John')
# #%%
# # 1~n까지의 합을 구해주는 함수
#
# def get_total_from1(end):
#     total=0
#     for i in range(end):
#         total = total+1
#     return total
#
# print(get_total_from1(10))
# #%%
# # 1~100까지 중 n의 배수를 print()로 출력하는 함수
# def multiply(num):
#     for i in range(1, 100):
#         if (i + 1) % num == 0:
#             print(i + 1)
#
# multiply(10)
# #%%
# # 세 정수의 뺄셈 함수
# def subtract(num1, num2, num3):
#     sub = num1 - num2 - num3
#     return sub
#
# print(subtract(10,2,3))
#
# #%%
#  문자열을 입력받고 원하는 문자의 개수를 구해주는 함수
#  def get_count_of_result(target, keyword):
#      # return len([i for i in target if i == keyword])
#      count = 0
#      for i in target:
#          if i == keyword:
#              count += 1
#      return count
#
# #%%
# '''
#     문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고,
#     만약 해당 문자가 없으면 -1을 리턴하는 함수
# '''
def input_text(str1, str2):

    for i in range(len(str1)):
        if str2 == str1[i]:
            return i
    return -1


print(input_text('바노노나나', '나'))

#
#%%
def find(target, keyword):
    for i in range(len(target)):
        if target[i] == keyword:
            return i
    return -1

# def find(target, keyword):
#     # for i in range(len(target)):
#     #     if target[i] == keyword:
#     #         return i
#     #         break
#     # return -1
#
#     # result = -1
#     # for i in range(len(target)):
#     #     if target[i] == keyword:
#     #         result = i
#     #         break
#     #
#     # return result
#
#     # 초보자용(참고용)
#     result = 0
#     for i in range(len(target)):
#         if target[i] == keyword:
#             result = i
#             break
#         else:
#             result = -1
#
#     return result
#
# # result = divide(10, 3)
# # if result:
# #     value, rest = result
# #     print(f'몫: {value}, 나머지: {rest}')
# # else:
# #     print('0으로 나눌 수 없습니다.')
# #
# # print_from1_to10()
#
# # print_time_from1_to100(7)
#
# print(find('apple', 'z'))