# 연습1)
# try:
#     number = int(input('정수를 입력하세요'))
# except ValueError as e:
#     print('정수만 입력해주세요')
# print('반드시 실행되어야 할 문장')
#

# 연습2)
# try :
#     print(10 / 0)
# #except ZeroDivisionError as e:
# #except ZeroDivisionError :
# except Exception :                  # Exception은 모든 에러의 부모이다.
# #    print(e)    # 오류메시지는 str로 재정의
#     print('0으로 나눌 수 없습니다.')


# 연습3)
# datas = [1, 2, 3]
# try:
#     print(datas[3])
#     # 위의 문장에서 오류가 발생하지 않는다면 실행된다.
#     print('오류가 없어요')
# except ValueError:
#     pass
# except IndexError:
#     print('인덱스를 확인해주세요')
# else: # try에 작성한 문장에서 오류가 발생하지 않는다면 실행된다.
#     print('오류가 없어요')
# finally:                        # 오류가 발생해도 실행된다.
#     print('반드시 실행되어야 하는 문장')


# 연습4)
# 만약에 닉네임이 비속어일 경우 에러발생
# nickname = input('닉네임')
# if nickname == '멍청이':
#     raise RuntimeError # -> 정확히 무슨 에러인지 판단하기 힘듬

# 오류가 나는 상황이 아닌데 오류를 발생시키고 싶을땐 raise


class BadWordError(Exception):
    def __str__(self):
        return '비속어는 사용할 수 없습니다.'

def check_bad_word(message):
    if '멍청이' in message:
        raise BadWordError

chat = input('채팅 : ')
try:
    check_bad_word(chat)
    print(chat)
except BadWordError as e:
    print(e)
