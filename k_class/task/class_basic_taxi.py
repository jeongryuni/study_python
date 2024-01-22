# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 1. 택시 객체 생성 시 승객 별로 돈과, 거리를 받아서 생성
# 2. 택시 객체 생성 시 택시 수익을 초기화한다.

# 1. 거리에 따른 요금 계산 메소드 정의
# 2. 거리에 따른 요금 계산 메소드 정의(승객의 돈과 거리를 전달받는다)
# 거리에 따른 잔돈 계산 메소드 정의

# 1.
class Taxi:
    # 정적 변수 (공통적으로 적용)
    default_fare = 5000
    default_distance = 2
    fare_per_km = 1000

    def __init__(self, money, distance):
        self.money = money
        self.distance = distance

    def calculate_fare(self):
        # 총 요금을 기본요금으로 설정
        cost = Taxi.default_fare
        # 입력받은 거리가 기본 주행 거리보다 크다면 (추가요금이 나온경우)
        if self.distance > Taxi.default_distance:
            # 거리당 발생한 추가요금을 총 요금에 더해준다
            cost += (self.distance - Taxi.default_distance) * Taxi.fare_per_km

        return cost

    def get_change(self):
        return self.money - self.calculate_fare()

# money: 지불한 돈, distance: 이동한 거리
taxi = Taxi(20000, 3)
print(f'택시 요금: {taxi.calculate_fare()} 남은 돈: {taxi.get_change()}')

taxi = Taxi(20000, 10)
print(f'택시 요금: {taxi.calculate_fare()} 남은 돈: {taxi.get_change()}')

# 2.
class Taxi:
    default_fare = 5800
    default_distance = 2
    fare_per_km = 1000

    def __init__(self):
        # 손님이 없을 때
        self.income = 0

    def calculate_fare(self, money, distance):
        cost = Taxi.default_fare
        # distance는 함수에서 사용하므로 self.을 붙이지 않음
        # cost = + 기본요금 (거리 - 택시 기본주행거리) * km당 요금
        # 거리 발생 추가요금을 총 요금에 더해준다
        if distance > Taxi.default_distance:
            cost += (distance - Taxi.default_distance) * Taxi.fare_per_km

        self.income += cost  # 손님이 타면 총 요금수익이 증가

        # get_change는 단독으로 쓸 일이 없으니 클로져 사용
        def get_change():           # 손님의 잔돈 계산
            return money - cost     # 손님의 돈 - 요금

        return cost, get_change()   # 요금과, 잔돈을 리턴받음


taxi = Taxi()
print(taxi.calculate_fare(20000, 1))  # 손님1명
print(taxi.calculate_fare(30000, 10)) # 손님 2명
print(taxi.income) # 총수익








