# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트
# 전체 내용을 문자열로 가져오기: file.read()

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""
# with 문을 사용하면 with 문에 속해 있는 문장을 벗어나는 순간, 열린 파일 객체 f가 자동으로 닫힌다.
with open('alice.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()

temp = ""                       # 임시 저장공간
for character in content:       # content를 반복문을 돌려 한글자씩 검사
    if 'a' <= character <= 'z': # 만약 문자가 a부터 z사이에 있는 문자라면
        temp += character       # temp에 문자를 담고
        continue                # 문자를 담았다면 아래 temp == " "는 실행하지 않고 넘어감.
    temp += " "

content = temp                  # 문자열을 담은 temp를 다시 content에 저장


# 내용을 공백으로 분리하고 글자수가 두개이상이면 word에 담는다.
# word를 반환하면서 리스트 형태가 풀렸기 떄문에 다시 리스트 형태로 바꿔준다.
words = [word for word in content.split() if len(word) >= 2]

# 컴프리헨션을 푼 식
# content = content.split()
# if len(content) >= 2:
#     words = content
# print(words)

result = {}                     # 빈칸의 딕셔너리 생성
for word in words:              # 리스트를 반복하면서 단어를 하나씩 가져옴
    if result.get(word) is not None: # 만약 딕셔너리 안에 word(단어)가 있다면
        result[word] += 1            # 딕셔너리에 접근해서 +1 (수정)

    else:                            # word(단어)가 없다면
        result[word] = 1             # 딕셔너리의 키로 존재하지 않으니 키 생성(생성)

result = {
    word: result[word]
    for word in result              # 딕셔너리를 반복하여 키를 하나씩 검사
    if result[word] >= 100          # 만약 단어 빈도수가 >= 100이상일 경우
}                                   # 딕셔너리 [키]word : [값]result[word]으로 담음


# 정렬
sorted_key = sorted(result, key=result.get, reverse=True)
for key in sorted_key:
    print(key, result[key])
#
# sorted(가져올 데이터, key= 정렬을 어떤것으로 기준으로 할지 함수형태로 전달)
# result는 딕셔너리 변수이므로 result.get은 딕셔너리 클래스의 get()메소드
# 따라서 딕셔너리는 키:밸류 형식으로 값들이 들어있는데, 이것을 정렬할때 key에 아무것도 전달하지 않으면 딕셔너리의 키를 기준으로 정렬함
# 여기서는 key가 아닌 value(단어의 빈도 수)를 기준으로 정렬하기 위해
# key=에 result.get 함수를 전달하여 sorted가 정렬하려고 딕셔너리의 키를 하나씩 받아올 때마다
# 키 대신 result.get(키), 즉 value를 받아와 이를 기준으로 내림차순으로 정렬
#
#
#
# def change(data):
#     return data * -1
#
# datas = [1, 2, 3, 4]
#
# print(sorted(datas, key=change))

# print(list({"A": 1, "B": 2, "C": 3}))