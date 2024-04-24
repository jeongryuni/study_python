'''
실습 설명
앞선 실습에서 vocabulary.txt라는 파일을 만들었죠?
이 파일에는 우리가 암기하고 싶은 단어들이 정리되어 있는데요.
이번에는 이 파일의 단어들을 가지고 학생들에게 문제를 내는 프로그램을 만들려고 합니다.

프로그램은 터미널에 한국어 뜻을 알려 줄 것이고,
사용자는 그에 맞는 영어 단어를 입력해야 합니다.
사용자가 입력한 영어 단어가 정답이면 맞았습니다!라고 출력하고, 틀리면 아쉽습니다. 정답은 OOO입니다.가 출력되어야 합니다.

문제를 내는 순서는 vocabulary.txt에 정리된 순서입니다.

실습 결과
고양이: cat
맞았습니다!

사과: fruit
아쉽습니다. 정답은 apple입니다.

교회: church
맞았습니다!

절: tample
아쉽습니다. 정답은 temple입니다.

지갑: wallet
맞았습니다!

책가방: bag
아쉽습니다. 정답은 backpack입니다.

비누: soap
맞았습니다!

자전거: bycicle
아쉽습니다. 정답은 bicycle입니다.
'''
voca = []

with open('vocabulary.txt', 'r') as f:
    for line in f:
        Line_strip = line.strip()
        Line_split = Line_strip.split(':')

        eng = Line_split[0]
        kor = Line_split[1]
        user = input(f'{kor}:')

        if eng == user:
            print('맞았습니다')
        elif user == 'q':
            break
        else:
            print(f'아쉽습니다. 정답은 {Line_split[0]} 입니다.')



