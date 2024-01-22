# 인간(부모)
# 이름, 나이

# 걷기(walk)
# '두 발로 걷습니다' 출력
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print('두 발로 걷습니다.')


# 원숭이(자식)
# 이름, 나이, 동물원 이름

# 걷기(walk)
# '두 발로 걷습니다', '네 발로 걷습니다' 출력
class Monkey(Person):
    def __init__(self, name, age, zoo):
        super().__init__(name, age)
        self.zoo = zoo

    def walk(self):
        super().walk()
        print('네 발로 걷습니다.')



kingkong = Monkey('콩순이', 90, '에버랜드')
kingkong.walk()



# class Animal:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def run(self):
#         print('달리기')
#
#
# class Dog(Animal):
#     def __init__(self, name, age, gender, zoo):
#         super().__init__(name, age, gender)
#         super().run()
#         print('걸어다닌다')
#         self.zoo = zoo
#
# ruby = Dog('ruby', 20, '여','에버랜드')
# ruby.run()