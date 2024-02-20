# with open('new_file.txt', 'w') as f:
with open('new_file.txt', 'a') as f:
    f.write('Hello\n')
    f.write('이정륜\n')
    # \n을 이용해 줄 바꿈
    # 덮어 쓰는 것이 아닌 추가를 하려면 'w'가 아닌 'a'를 사용
    # 파일이 없어도 w대신 a를 사용할 수 있다.
