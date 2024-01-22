# # print("ABC")
# # # 문자열 문자:3개 - 3칸
# # # 문자열은 내부적으로 리스트를 사용한다.
# # # 문자열은 리스트이다.
# #
# # print(list("ABC")) #['A', 'B', 'C']
#
# # for i in "ABC":
# #     print(i)
# # # 출력
# # #A
# # #B
# # #C
# # # 문자열도 순서가 있다.
#
#
# # upper(), lower()
# # 빅데이터들은 규칙을 찾기 힘들기 때문에
# # 대문자나 소문자로 변환하여 규칙을 찾기 쉽게 해준다.
#
# print("Apple123!@#".upper()) #APPLE123!@#
# print("Apple123!@#".lower()) #apple123!@#
#
# # split()
# data = "사과, 바나나, 파인애플, 포도, 복숭아"
# print(data.split(",", maxsplit=2)) #maxsplit 가 주어지면 최대 maxsplit 번의 분할 수행
# maxsplit=2 을써서 ','로 구분점을 쓰면 컴마2개 이후엔 다음 문자열은 구분하지말고 붙여서 출력

# print("A B C D E F".split())
# print("A         B".split())
# print("A   B".split(" ")) # 공백을 구분점으로 삼으면 빈칸이 리스트에 들어감
#
#
# # join() : 문자들을 연결할 때 사용한다.
# print(":".join(['a','b','c'])) #문자가 : 으로 연결되어서 나온다.
# print("".join(['a','b','c'])) #문자가 붙어서 나온다.
#
# # replace('기존값', '새로운 값')
# # 문자를 다른값으로 변경할 때  사용.
# print("A b C d".replace(" ", "")) #공백을 빈 문자열로 바꾸기 #AbCd
# print("안녕, 반가워!".replace('!', '?')) #느낌표를 물음표로 바꾸기 #안녕, 반가워?
#
# # strip(), lstrip(), rstrip() : 해당 문자열의 공백을 없애준다. / 앞 뒤 공백을 제거할 때 보통 사용한다.
# print("A           b          c        ".strip())   # A           b          c
# print("A           b          c        ".strip(" ")) # A           b          c
# print("apple".strip("a")) # strip은 맨 앞과 맨뒤 공백제거 #pple
#
# # index() : 찾고자 하는 값이 없으면 오류가 발생한다.
# print("ABC".index("A")) # 0
# # print("ABC".index("Z")) # 오류
#
# # find() : 찾곶 하는 값이 없으면 -1을 가져온다.
# print("ABC".find("A")) # 0
# print("ABC".find("Z"))  # -1
#
# # in : 값의 유무 검사
# print("A" in "ABC") # Ture
# print("Z" in "ABC") # False
#
# # count() : 전달한 값이 몇 개 있는지 검사(카운트)
# print("owdjqidjoiwjdskqodwqwndnfeofnonqnwxonowfe".count("o")) # 7
#
# #
s = "189,000원"
print("".join([i for i in s if '0' <= i <= '9']))
print("".join(i for i in s if '0' <= i <= '9')) #join은 순서가

# s에서 문자열을 뽑아 i에 값을 넣고 만약(if) i가  '0'<=i<='9' 사이면
# i에 값을 전달해라 그리고 join으로 ""하여 문자열을 붙여라

#next는 값을 하나씩 가져옴
print(next(i for i in s if '0'<= i <= '9')) # 1

# 문자열 안의 정수들은 조건식에서 사용하면 자동적으로 정수로 바뀐다. 정수로 비교가 됨.
# for i in s:
#     if '0' <= i <= '9':
#         print(i, end ="")


#print(ord('0')) #아스키코드
# '0' -> 48 로 기억(아스키코드)로 통해 비교가 됨
# '1' -> 49 ....