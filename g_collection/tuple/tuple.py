# mutalble : 변할 수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10
print(data_list2) # [10, 2, 3, 4]
print(data_list1) # [10, 2, 3, 4]

# immutable : 변할 수 없는
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1
#data_tuple2[0] = 10 # 튜플은 값을 변경할 수 없다.
data_tuple2 = data_tuple1 + (5, 6)
print(data_tuple2)      # (1, 2, 3, 4, 5, 6)
print(data_tuple1)      # (1, 2, 3, 4)

datas = 1 ,2 # 소괄호 없이도 튜플 생성 가능
print(type(datas))       # <class 'tuple'>
print(datas[0])         # 1
# print(data_tuple2) # 오류
# 리스트는 길이 제한을 주기에는 적합하지 않다.
# 리스트는 if문으로 제한을 줄 수있다.
# 하지만 효율성이 떨어진다.

# 튜플의 데이터를 변환하고 싶다면
# list로 타입을 변경
test = list(data_tuple2)
test[0] = 10
print(test) # [10, 2, 3, 4, 5, 6]

# 값이 하나만 있을때 콤마만 써주면 튜플
ERROR_CODE = 1,
print(type(ERROR_CODE)) # <class 'tuple'>
print(type(ERROR_CODE)[0]) #tuple[0]

# 개발자들끼리 만든 약속
# 변수 상수는 대문자로 약속
# 대문자_상수는 변경X
