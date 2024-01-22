# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).
class User:
    # private: 자신의 클래스에서만 접근 가능
    # 1. 외부에서 접근하지 말자!
    # 2. 외부에서 접근할 때 꼭 메소드로 접근하자!
    __user_number = 0

    def __init__(self, user_id, user_password, user_name):  # (회원id , 회원pw, 회원이름 )
        User.__user_number += 1                 # 유저 추가시 번호 + 1
        self.user_number = User.__user_number
        self.user_id = user_id
        self.user_password = user_password
        self.user_name = user_name

    @staticmethod                           # 스태틱메소드 ( private 에 접근하기 위한 함수 )
    def get_number():                       # self를 쓰지 않을때, 한번에 모든 객체에 적용할 기능
        return User.__user_number           # private : 외부에서 접근을 막아주는 방식(함수를 만들어야 접근가능)

    @classmethod                            # 클래스메소드
    def set_admin(cls, **kwargs):           # 클래스메소드 : 래핑을 할때 사용, 기존 생성자에 추가할 기능을 작성한다.
        kwargs['user_id'] = 'admin_' + kwargs['user_id']   # 추가 기능 : 관리자 회원가입시 'admin_'이 user_id앞에 추가
        return cls(**kwargs)                # 클래스메소드 리턴함으로써 기능이 추가됨


user = User('hds', '1234', '한동석') # 일반유저 회원가입 ( admin_추가 x )
print(user.user_id)                                               # 출력값 : hds

admin = User.set_admin(user_id='hds', user_password='1234', user_name='한동석') # 관리자 회원가입 ( admin_추가 o )
print(admin.user_id)                                                          # 출력값 : admin_hds


print(User.get_number())    # 생성된 ㄱ유저의 수  : 2



