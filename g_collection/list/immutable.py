import copy

# 얕은 복사 : 기존 값을 복사해서 새롭게 만들어내는 것을 의미한다.
# 얕은 복사 사용 시, 두 번째 접근 부터는 불변성이 보장되지 않는다.
# 새로운 주소를 할당하기 때문에, 불변성이 보장된다.


# 얕은복사 예)
# 얕은 복사
datas = [1, 2, 3]
datas_copy = copy.copy(datas)  # 복사하고 싶은 리스트를 입력하면 위에있는 리스트주소와 주소가 다른 리스트가 카피됨(불변성 보장)=>원본 유지
# datas_copy = datas
# print(datas is datas_copy) # False <class 'type'>
datas_copy[0] = 10
print(datas)
print(datas_copy)


# 얕은 복사 예1)
datas = [1, 2, 3]
datas_copy = datas[:]
datas_copy[0] = 10
print(datas)
print(datas_copy)


# 얕은복사 예2)
# 얕은 복사
# 얕은 복사 사용 시, 두 번째 접근부터는 불변성이 보장되지 않는다.
datas = [1, [1, 2, 3], [4, 5, 6]]
datas_copy = copy.copy(datas)
datas_copy[0] = 10
print(datas)
print(datas_copy)

datas_copy[1][0] = 10
print(datas)
print(datas_copy)

#깊은 복사 사용 시, 깊은 접근까지 모두 불변성이 보장된다.
# 너무 깊은 구조에서 사용할 때에는, 메모리 소모량이 증가하기 때문에,
# 불변성이 보장될 필요가 없을 때에는 사용하지 않는 것이 좋다.

# 깊은 복사
datas = [1, [1, 2, 3], [4, 5, 6]]
datas_copy = copy.deepcopy(datas)
datas_copy[1][0] = 10
print(datas)
print(datas_copy)