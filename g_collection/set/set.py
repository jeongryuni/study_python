# 중복이 없고, 순서가 없다.
# 값이 있는지 없는지 검사
world_set = {'korea', 'america', 'japan', 'china'} # 중괄호에 값이 하나씩 연결되어 있으면 set
print(type(world_set)) # <class 'set'>
print(len(world_set)) # 4
#print(world_set[1]) # 오류 -> 순서가 없기때문에 데이터를 가져올 수 없다.
world_set.add('korea') # 중복된 값은 데이터에 추가되지 않는다.
print(world_set)    #{'china', 'korea', 'japan', 'america'}

# set의 데이터를 가져오는 방법
# 다른 구조로 형변환을 시킴
# print로 출력했을때 나오는 데이터 값은 set을 다른 자료구조로 가져온 다음 {}로 닫아준 것.


data = [1, 2, 3, 1, 1, 4, 4, 5]
print(list(set(data))) #[1, 2, 3, 4, 5]
