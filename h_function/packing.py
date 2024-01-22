# # unpanking : 값을 풀어서 적는 것
# def get_Total(number1, number2, number3):
#     return number1 + number2 + number3

# packing : 값을 묶어서 적는 것
def get_total(*numbers): # *이 있다면 패킹 : 여러개 선언해야 하는것을 한번에 묶어서 받음
    # 외부에서 전달받은 값들이 numbers(튜플)에 튜플형태로 저장된다.
    print(type(numbers))
    total = 0
    for number in numbers:
        total += number

    return total

#여러개의 값을 콤마로 구분하여 전달한다.
total = get_total(1, 2, 3, 4, 5)
print(total)

# *을 사용하면 get_total이 튜플형태로 한번에 들어간다
numbers = [1, 2, 3, 4, 5]
total = get_total(numbers)
print(total) # TypeError: unsupported operand type(s) for +=: 'int' and 'list'
# 자동으로 여러개 값을 받기때문에
# 리스트로 받음
# 여러개의 값을 하나로 묶어서 전달하게 되면, packing으로 인해 첫번째 방에 통채로 들어가게 된다.
# 즉, 결과는 다음과 같다 ([1, 2, 3, 4, 5],)
# 따라서 내부의 요소는 각각 전달하고 싶다면, 앞에 *을 작성해야한다.
# numbers = [1, 2, 3, 4, 5]
# total = get_total(*numbers)# 데이터가 묶어서 왔을때 *을 사용
# print(total)
# # 튜플로 한번에 값을 받음


# 국어 영어 수학 점수를 전달받은 뒤 총점을 출력하는 함수
# packing으로 제작하기
def get_total(name, *scores): # 반드시 받아야하는 매개변수는 packing앞에 작성한다
    print(name + '님')
    total = 0
    for score in scores:
        total += score
    return total

scores= [100,40,50]
print(get_total('류니', 100, 40, 50))



# 문자열에서 'A'가 몇개 있는지 검사하는 함수
# packing으로 제작하기
#%%
def get_count_of_A(*strs):
    result=[]
    count = 0
    counts = []
    for str in strs:
        for s in str:
            if s == "A":
                count+= 1
        counts.append(count)
        count=0

print(get_count_of_A("ABC","AAB","AAA"))


#%%
def get_count_of_A(*star):
    return [str.count('A') for str in strs]

print(get_count_of_A("ABC", "AAB", "AAA"))