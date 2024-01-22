class A:
    pass

class B(A):
    pass


a = A()
b = B()

print(isinstance(a, A)) # a가 A타입인지 #Ture
print(isinstance(b, B)) # b가 B타입인지 #Ture

# 모든 자식은 부모타입이다.
print(isinstance(b, A)) # Ture 부모의 타입을 비교하기
# 부모는 절대 자식타입이 될 수 없다.
print(isinstance(a, B)) # False

