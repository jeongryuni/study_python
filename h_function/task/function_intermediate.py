# 실습 1번
# user_info = [
#     {'number': 1, 'name': 'john'},
#     {'number': 2, 'name': 'mike'},
#     {'number': 3, 'name': 'ted'},
#     {'number': 4, 'name': 'lindy'},
#     {'number': 5, 'name': 'adam'},
# ]
#
#
# # 추가(초보자용)
# # def insert(*, number, name):
# #     '''
# #
# #     :param number: 회원 번호
# #     :param name: 회원 이름
# #     '''
# #     user_info.append({'number': number, 'name': name})
#
#
# # 추가
# # 회원 번호는 자동 증가한다.
# number = 5
# def insert(name):
#     global number
#     number += 1
#     user_info.append({'number': number, 'name': name})
#
#
# # 목록
# def select_all():
#     return user_info
#
#
# # 조회(번호로 조회)
# def select(number):
#     for user in user_info:
#         if user['number'] == number:
#             return user
#     return {}
#
#
# # 수정(번호로 이름 수정)
# def update(**kwargs):
#     '''
#
#     :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
#     '''
#     select(kwargs.get('number'))['name'] = kwargs.get('name')
#
#
# # 삭제(번호로 삭제)
# def delete(number):
#     del user_info[user_info.index(select(number))]
#

#%% 실습2번
### 내가 만든 풀이
post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
number_list = 5 # 전역변수
def insert(number, title, content, file, read_count=0):
    '''

    '''
    global number_list
    number_list += 1
    post_info.append({'number': number, 'title': title, 'content': content, 'file': file, 'read_count': read_count})

insert(number= 6, title='테스트 제목6', content= '테스트 내용6', file= '/usr/post/file/img005.png')

#목록(최신순으로 조회)
def select_all():
    return post_info[::-1]

print(select_all())
#조회(번호로 조회, 조회수 1 증가)
def select(number):                 #조회한 정보
    for user in post_info:
        if user['number'] == number:
            user['read_count'] += 1
            return user

print(select(1))
print(select(1))

#수정(번호로 정보 수정)
# def update(**kwargs):
#
#         select(kwargs.get('number'))['number'] = kwargs.get('number')
#         select(kwargs.get('number'))['title'] = kwargs.get('title')
#         select(kwargs.get('number'))['content'] = kwargs.get('content')
#         select(kwargs.get('number'))['file'] = kwargs.get('file')
#         select(kwargs.get('number'))['read_count'] = kwargs.get('read_count')
#
# update(number= 5, title='테스트 제목7', content= '테스트 내용7', file= '/usr/post/file/img007.png', read_count= 0)
# print(post_info)

def update(**kwargs): #수정이 다 끝난 값을 받음

    select(kwargs.get('number'))['number'] = kwargs.get('number')
    select(kwargs.get('number'))['title'] = kwargs.get('title')
    select(kwargs.get('number'))['content'] = kwargs.get('content')
    select(kwargs.get('number'))['file'] = kwargs.get('file')
    select(kwargs.get('number'))['read_count'] = kwargs.get('read_count')

update(number=5, title='테스트 제목7', content='테스트 내용7', file='/usr/post/file/img007.png', read_count=0)
print(select_all())


# 삭제(번호로 삭제)
def delete(number):
    del post_info[post_info.index(select(number))]
delete(number=1)
print(select_all())


#%% 실습 2번
# 선생님 풀이
# 하단에 실행함수 입력된 셀

post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

# 전역변수
number = 5

# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
def insert(**kwargs):
    '''

    :param kwargs: {'title': '게시글 제목', 'content': '게시글 내용', 'file': '파일의 경로'},
    :return:
    '''
    global number
    number += 1
    post = {
        'number': number,
        'title': kwargs.get('title'),
        'content': kwargs.get('content'),
        'file': kwargs.get('file'),
        'read_count': 0
    }
    post_info.append(post)


# 목록(최신순으로 조회)
def select_all():
    return post_info[::-1]      # 딕셔너리[::-1] 슬라이스로 스텝-1로 인덱스를 거꾸로 뒤집어 최신순을 만듬


# 조회(번호로 조회, 조회수 1 증가)
def read(number):
    post = select(number)       # 번호로 조회하는 함수를 post변수에 담음
    post['read_count'] += 1     # 입력한 숫자의 게시글 조회수 + 1
    return post

# 조회(번호로 조회)
def select(number):
    for post in post_info:              # post_info 딕셔너리 반복 후 post에 담음
        if post['number'] == number:    # 만약 post 번호가 입력한 number와 일치할 때
            return post                 # post 리턴
    return {}                           # 일치하지 않으면 빈칸

# 수정(번호로 정보 수정)
def update(**kwargs):                    # 수정이 다 끝난 값을 받음 (**kwargs 여러개의 값을 한번에 선언 )
    post = select(kwargs.get('number'))  # 번호로 조회하는 함수를 post변수에 담고 *******
    post['title'] = kwargs.get('title')  # 입력한 번호의 타이틀 수정
    post['content'] = kwargs['content']  # 입력한 번호의 콘텐트 수정  ??? content만 get을 안쓴이유 =>선택사항
    post['file'] = kwargs.get('file')    # 입력한 번호의 파일 수정


# 삭제(번호로 삭제)
def delete(number):
    del post_info[post_info.index(select(number))]  # 목록[목록.인덱스[번호]]
                                                    # 입력한 번호의 목록[인덱스 값]을 찾아서 삭제

insert(title='테스트 제목6', content='테스트 내용6', file='')
print(select_all())
print(read(5))
print(read(5))
print(read(5))
post = read(5)
post['title'] = '수정된 제목'
update(**post)
print(read(5))
delete(5)
print(select_all())

