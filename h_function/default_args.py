# # 값을 만약 매개변수로 전달하지 않았을 경우
# # 기본 값을 설정할 수 있고, arg=value로 작성한다.
#
# def sub(number1, number2, number3, number4=0): #값이 들어올수 있고 안들어올수 있을땐 초기값 = 0 # 값이 들어오면 그 값으로 대체됨
#     return number1 - number2 - number3 - number4
#
# result = sub(1,2,3)
# print(result)

# 실습
# 이름을 전달받지 못하면 '익명'으로 대체하고,
# 나이를 전달받지 못하면 0으로 대체한다.
def get_info(name= '익명', age=0):
    return {'name': name, 'age': age}

print(get_info(name = '류니'))
print(get_info(age = '류니'))