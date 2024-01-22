# 인덱스 슬라이싱
animals = ['dog', 'dog', 'cat', 'bird', 'fish']


# list[inclusive_start=0 : exclusive_end =len(list): step = 1 => list
print(animals[0])
print(animals[0:3])
print(animals[1:4])
print(animals[:2])
print(animals[2:])


# food = ['noodle', 'meat', 'bread', 'chicken']
# print(food[:3:2]) # [start, end, step] 2씩 증가 [0],[2] 출력
# print(food[2::2]) # 2부터 끝까지 2씩 증가 #step은 웬만해서 쓰지 않는다.
#
# # 역순 출력
# print(food[::-1]) # step이 -1씩 증가하기 때문에 역순으로 나옴


# 실습
number_list = list(range(1, 11))
print(number_list)

# [1, 3, 5, 7, 9]
print(number_list[::2]) # 1부터 2씩 증가
# [6, 5, 4, 3, 2]
print(number_list[5:0:-1]) #6이 인덱스[5]에 있어 [5]부터 시작 2의 인덱스[1]이지만 마지막값 포함안하기 때문에 [0]
# [2, 4, 6]
print(number_list[1:6:2])  # 인덱스[1]에 2가있고 [6]에는 6이 있으므로 스텝2씩 증가
# [2, 3, 4, 5, 6, 7]
print(number_list[1:7])    # 2의 인덱스[1], 7의 인덱스[7]


animals = ['dog', 'dog', 'cat', 'bird']
zoo = ['panda', 'giraffe']

animals[1:2] = zoo                          # 값만 값에 추가 시키려면 슬라이싱
print(animals)

animals.insert(animals.index('dog') + 1, 'giraffe')
print(animals)

animals.insert(animals.index('dog')+ 1, zoo)
print(animals)                                  # 리스트를 통채로 값에 넣고 싶으면 insert



# 슬라이싱, insert, del 를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']
animals = ['dog', 'dog', 'cat', 'bird']


del animals[animals.index('cat')]
print(animals) #['dog', 'dog', 'bird']

animals[-2:-3:-1] = ['whale']
print(animals) #['dog', 'whale', 'bird']

animals.insert(animals.index('dog')+1, 'fish')
print(animals) #['dog', 'fish', 'whale', 'bird']

animals.insert(animals.index('dog')+1, 'hamster')
print(animals) #['dog', 'hamster', 'fish', 'whale', 'bird']

animals[1:3] = ['hamster', 'fish', 'dog']
print(animals) #['dog', 'hamster', 'fish', 'dog', 'whale', 'bird']


