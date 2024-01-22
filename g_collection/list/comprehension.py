# Comprehension : 컴프리헨션(어떤 뜻을) 내포
# 반복하거나 특정 조건을 만족하는 list를 보다 쉽게 만들어 내기 위한 방법

# List Comprehension
#
# [표현식 for 항목 in iterator (if 조건)]
# iterator란 순서가 있는 것
#
# number_list = [1, 2, 3, 4]
# result_list = [num*3 for num in number_list] # 4번 반복 for뒤는 반복문 for 앞은 결과과 리스트에 담김
# print(result_list)

# number_list = [1, 2, 3, 4]
# # [6, 12]
# result_list = [number*3 for number in number_list if number %2 == 0]  # number은 짝수만 나옴
# print(result_list)

# [표현식 if 조건 else 표현식 for 항목 in iterator]
# [1, 6, 3, 12]
# number_list = [1, 2, 3, 4]
# result_list = [number * 3 if number % 2 == 0 else number for number in number_list]
# print(result_list)

##실습

# 1.아래의 list에서 양수만 추출한 뒤 새로운 리스트에 담기
number_list = [10, 20, 30, -20, -3, 50, -70]
result_list = []
result_list = [number for number in number_list if number >0]
print(result_list)
#
# number을 가져올건데 in number_list에서 가져올 것이다.
# 양수만 가져올 조건은 맨 뒤 입력 if 만약에 number>0보다 큰가?

#2. n개의 0으로만 채워진 list
message = '생성할 리스트의 칸 수 입력 : '
n = int(input(message))
zero_list = [0 for _ in range(n)]
print(zero_list)

# zero_list = [0] * n

#3. 제곱의 결과가 10보다 큰 결과만 담은 list
number_list = [1, -2, 3, -4, 5]
sq_list = [number for number in number_list if number**2> 10]
print(sq_list)
# number_list에서 number에 값을 하나하나 담고 number를 제곱했을때 10보다 크면 그때 number을 가져옴


#4.  0~9까지 중 3의 배수만 담은 list
number_list4 = [num for num in range(10) if num % 3 == 0]
print(number_list4)
# range(10)에서 num에 값을 담고 num을 3으로 나누었을때 0 이 나오는 값을 num에 담음