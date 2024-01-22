class NameCard:
    def print_info(self, name):
        print(name)

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def __del__(self):
        print('del')


with NameCard() as name_card:
    name_card.print_info('이정륜')

# 출력값
# enter
# 이정륜
# exit
# del

# 따라서 with문을 사용하면 EXIT부분에서 파일.close()를 한다.
