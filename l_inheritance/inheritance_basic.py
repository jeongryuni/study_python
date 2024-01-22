class TV:
    def __init__(self):
        self.power = False
        self.channel = 1
        self.volume = 1

    def display_info(self):
        print(f'전원: {self.power}')
        print(f'채널: {self.channel}')
        print(f'볼륨: {self.volume}')


tv = TV()
tv.display_info()
# 전원: False
# 채널: 1
# 볼륨: 1


class SmartTV(TV):              # 부모(TV) 상속받음
    def __init__(self):
        # 직접 자식 생성자를 선언하면, 반드시 부모 생성자도 직접 호출한다.
        super().__init__()  # 부모의 것을 가져옴
        self.ip = "192.168.1.1" # 자식에서 새로 생성된 기능

    def display_info(self):     #
        super().display_info()
        print(f'IP: {self.ip}')


smart_tv = SmartTV()
smart_tv.display_info()
# 전원: False
# 채널: 1
# 볼륨: 1
# IP: 192.168.1.1
