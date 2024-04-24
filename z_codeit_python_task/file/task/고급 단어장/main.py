import random

vocab = {}

with open('vocabulary.txt', 'r') as f:
    for line in f:
        Line_strip = line.strip()
        Line_split = Line_strip.split(': ')

        eng = Line_split[0]
        kor = Line_split[1]

        vocab[eng] = kor

keys = list(vocab.keys())
# print(vocab)
# print(len(keys))

while True:
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]

    user = input(f'{vocab[english_word]}: ')

    if user == english_word:
        print('맞았습니다.')

    elif user =='q':
        break

    else:
        print(f'정답은 {english_word}입니다.')
