# # 람다(lambda) : 이름이 없는 함수, 일회성
# # lambda 매개변수, ... : 리턴값

# 일반 함수
# def add(number1, number2):
#     return number1 + number2
# add(10, 5)
#
# 익명 함수
# lambda number1, number2: number1 + number2 # 람다는 함수가 들어갈자리에 한번만 사용할때 사용.
# add

# # lambda x: x +2
# # (매개변수)  (리턴값)
# #
# #
# # map(lambda x : x +2,)

# 사용 예시
#print(list(map(lambda num : num + 2, [1, 2, 3, 4])))  #[3, 4, 5, 6]

# [1,2,3,4]에서 요소를 num에 하나씩 가져와서
# num요소마다 + 2를 해줌
#
# datas = [2, 4, 6, 8]
#
# print(list(map(lambda x: x * 2, datas)))
#
# # '/app/game', '/app/news', '/app/fashion', '/app/ranking'
# urls = ['/game', '/news', '/fashion', '/ranking']
# print(list(map(lambda x : '/app'+ x, urls)))
#
# # filter(function, iterator)
# 1~10까지 중 짝수만 출력
print(list(filter(lambda number: number %2==0,[i+2 for i in range(10)])))#filter는 추려낼때/ map은 바꿀때
#

# '/app/game', '/app/news', '/app/fashion', '/app/ranking'
# 'game' 서비스를 제공하는 경로 찾기
urls = ['/app/game', '/app/news', '/app/fashion', '/app/ranking']
print(list(filter(lambda url: url.split('/')[-1] == 'game', urls)))
# ulrs에서 url로 가져오고 split으로 /로 나눈다.
# -1로 사용하는 이유는 마지막에 있는값을 찾아야하기 때문 = > 이 값이 game인지 찾는다
