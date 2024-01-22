# # animals = ["dog", "cat", "bird", "fish"]
# # print(animals)       # 값 확인
# # print(type(animals)) # 타입 확인
# #
# # # 인덱스로 접근
# # print(animals[1])   # cat
# # print(animals[2])   # bird
# #
# # # 음수 인덱스 기능(가장 마지막부터 순서대로 앞으로 이동한다)
# # # 게시글 중 최신글을 불러올때 사용
# # print(animals[-1]) # fish
# # print(animals[-2]) # bird
# #
# # # len()
# # print(len(animals)) # 4
# #
# # # append()
# # animals.append("panda")
# # print(len(animals)) # 5
# # print(animals)
# #
# # animals.append("cat") # 리스트는 중복을 신경쓰지 않는다.
# # print(animals)
# #
# # # insert()
# # animals.insert(1, "dog")
# # print(animals)
# #
# # # remove()
# # animals.remove('fish')
# # print(animals)
# #
# # # del()
# # #del(animals[1])
# # del animals[1]
# # print(animals)
# #
# # # # clear
# # # animals.clear()
# # # print(animals)
# #
# # # index()
# # print(animals.index('bird'))
# # #print(animals.index('tiger')) # 리스트에 값이 들어있지 않아 오류가 남.
# #
# # # 수정
# # index = animals.index('bird')
# # animals[index] = 'lion'
# # print(animals)
# #
# # # 그 외
# # animals = ['dog', 'cat', 'bird', 'fish']
# # print(animals * 2)
# #
# # print("dog" in animals) # True animals안에 dog가 있는지 확인
# # print("tiger" in animals) # False
# #
# # for i in animals:       #a animals안에 있는 값들이 순서대로 출력
# #     print(i)
# #
# #
# # for animal in animals:
# #     print(animal)
#
#
# ### 실습
# # 1~90까지 list에 담고 출력
# number_list = [0] * 90  # 리스트의 칸을 미리 만들기
#
# for i in range(len(number_list)):
#     number_list[i] = i + 1
#
# # 1~100까지 중 짝수만 list에 담고 출력
# number_list2 = [0] * 50  # 리스트의 칸을 미리 만들기
#
# for i in range(len(number_list2)):
#     number_list2[i] = (i + 1) * 2
# print(number_list2)
#
# #1~10까지 list에 담은 후  짝수만 출력
# number_list3 = [0] * 10
# for i in range(len(number_list3)):
#     number_list3[i] = i + 1
#     if i % 2 == 0:
#         print(i, end ='')
#
#
# num3 = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         num3.append(i)
# print(num3)
# #%%
# # 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
# panda = ['푸바오', '아이바오', '러바오']
#
# panda[0] = '후이바오'
# print(panda)
#
# panda.pop()
# print(panda)
#


#list 안에 list
number_list = [[1,3,5], [2,4,6]] # 2번 접근 []로 접근

#print(number_list[0][0])
leghth = len(number_list) * len(number_list[0]) # 2 * 3 = 6
#print(leghth)

for i in range(len(number_list)):
    for j in range(len(number_list[i])): #
        print(number_list[i][j])