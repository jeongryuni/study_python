# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구
hangul = "공일이삼사오육칠팔구"
data = 3519
print("".join(list(map(lambda s: hangul[int(s)], str(data)))))
# print("".join(list(map(lambda s: hangul[ord(s) - 48], str(data)))))

# string_change = {'삼':3,'오':5,'일':1,'구':9}
# print(list(filter(lambda string :string, string_change.values())))


# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# 위 경로 중 회원 서비스가 아닌 경로만 추출
# 1. 서비스명(user, post, order)으로 변경(map)
urls = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']
#print(list(map(lambda url: url[:url.index("/")], urls)))
# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
print(list(filter(lambda x: 'user' not in x, urls)))

# 출력 예시
# ['post', 'order', 'order', 'post']
urls = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']

#print(list(filter(lambda service: service != 'user', list(map(lambda url: url[:url.index("/")], urls)))))
