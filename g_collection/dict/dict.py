# student = {
#     "name": "이정륜",
#     "email": "wjdfbsdl4399@gmail.com"
# }
#
# print(student["name"])
# print(student.get('name'))
#
# # get()을 사용하면 key를 찾지 못했을 때 원하는 default 값으로 설정이 가능하며,
# # default 값이 없을 때에는 None을 가져온다.
# # print(student(pthne)) 오류
#
# print(student.get('phone'))
# print(student.get('phone','010101010101')) # 입력한 키: phone, 디폴트값
# # get으로 phone을 가져올때 존재하지 않는 키값이면 None이 출력된다.
# # 데이터가 없을때 없다는것을 알려준다.
#
#
# # 'name'의 key값이 이미 있기 때문에, 아래의 코드는 수정이다.
# student['name'] = '류니'
# print(student)
#
# # 'phone'이라는 키 값이 없기 대문에, 아래의 코드는 추가이다.
# student['phone'] = '010101010101'
# print(student)
#
# if 'email' in student: # 'email'이라는 키가 student에 있다면?
#     student['email'] = 'fbsl@gmail.com' # 수정
# else:
#     student['email'] = 'fbsl@gmail.com' # 추가
# print(student)
#
#
# my_dict = {
#    1:"이정륜",
#     "two":"25살",
#     False : [10, 20 ,30],
#     "row":[
#         {"name": "ted", "age": 40},
#         {"name": "jack", "age": 30},
#         {"name": "john", "age": 20}
#     ]
# }
# # row에 있는 회원 3명의 정보를 모두 출력
#
# if 'row' in my_dict:
#     print(type(my_dict['row']))
#     for data in my_dict['row']:
#         print(f'{data["name"]}, {data["age"]}')

# 1~10까지 중 홀수와 짝수가 있다.
# 사용자가 '짝수'를 입력하면, 짝수만 출력하고
# '홀수'를 입력하면, 홀수만 출력한다.
# dict를 사용한다.
# number_dict = {
#     '홀수': [i * 2 + 1 for i in range(5)],
#     '짝수': [(i + 1) * 2 for i in range(5)]
# }

# number_dict = {
#     True: [i * 2 + 1 for i in range(5)],
#     False: [(i + 1) * 2 for i in range(5)]
# }

# print(", ".join(map(str, number_dict[input('짝수 혹은 홀수: ')])))
# print(", ".join(map(str, number_dict[input('짝수 혹은 홀수: ') == '홀수'])))


# user = int(input())
# my_dict = {'짝수': [i for i in range(0,11) if i% 2 == 0 ],
#            '홀수': [i for i in range(0,11) if i% 2 == 1]
#            }
#
# if user % 2 == 0:
#     print(my_dict['짝수'])
# else:
#     print(my_dict['홀수'])

student = {
     "name": "이정륜",
     "email": "wjdfbsdl4399@gmail.com"
}

# key 분리
print(list(student.keys()))


# value 분리
print(list(student.values()))


# item 분리 (한 쌍씩 가져옴)
print(list(student.items()))
# 튜플로 출력
print(list(student.items()))
# list로 형변환


for key, value in student.items():
    print(key, value)