
# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

title = "또와 과일"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        # 사용자에게 상품명과 가격을 동시에 입력받는다(구분점은 공백문자).
        new_name, new_price = input(append_message).split()
        # 입력한 상품명이 기존 상품과 중복되지 없다면,
        if new_name not in name_list:
            # 이름 list에 추가
            name_list.append(new_name)
            # 가격 list에 추가
            price_list.append(int(new_price))
            # 오류 메세지를 출력하지 않기 위해서 continue를 작성해 즉시 다음 반복으로 skip
            continue
        else:
            # 입력한 상품명이 기존 상품과 중복되었다면,
            # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = append_error_message

    # 수정
    elif choice == 2:
        name = input(search_name_message_for_update)    # 수정할 상품명 입력
        if name in name_list:                           # 만약 name_list(상품리스트)안에 name(상품)이 존재한다면
            new_name, new_price = input(update_message).split()
            # input에 입력한 수정할 상품명과 가격을 split()으로 나누고 new_name와 new_price 변수에 각각 저장
            if new_name not in name_list:        # 만약 new_name과(수정한 상품명)이 name_list(상품리스트)에 존재하지 않는다면,
                index = name_list.index(name)
                # index 변수에 수정할 상품명의 인덱스를 저장함
                # 상품의 인덱스는 상품명과 가격과 index번호가 같으므로 상품명의 인덱스로 index를 뽑아쓰기 위해 저장
                name_list[index], price_list[index] = new_name, new_price
                #name_list[index], price_list[index]에 new_name,과 new_price를 저장
                continue # 오류 메세지를 출력하지 않기 위해서 continue를 작성해 즉시 다음 반복으로 skip
            else: # 입력된 상품명이 중복일때
                result_message = update_error_message2 # 수정실패 : 중복된 상품명 오류메시지
        else: # 상품목록에 수정할 상품명이 존재하지 않을 경우
            result_message = update_error_message1  # 수정실패 : 존재하지 않는 상품명 오류메시지

    # 삭제
    elif choice == 3:
        name = input(delete_message) # input값에 삭제할 상품명을 입력 후 name이라는 변수에 저장.
        if name in name_list:       # 만약 name이 name이 name_list에 존재한다면,
            index = name_list.index(name) # index라는 변수에 삭제할 상품명 인덱스를 저장
            del name_list[index]    #해당 인덱스 번호의 상품명과 가격 삭제
            del price_list[index]
            continue

        else:        #상품목록에 삭제할 상품명이 없다면 에러메세지 출력
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        choice = int(input(search_menu)) # input창에서 1:상품명과 2:가격중 어느 것으로 검색할 지 선택

        # 상품명으로 검색
        if choice == 1:
            name = input(search_name_message) # 검색할 상품 입력
            if name in name_list:   # 만약 입력한 상품이 nmae_list에 존재 한다면,
                index = name_list.index(name) # index라는 변수에 검색할 상품명의 인덱스를 저장
                print(f'{name_list[index]}, {price_list[index]}') # 검색한 상품의 name_list와 pirce_list 출력
                continue

            else: #상품목록에 상품명이 없는경우 -> 검색결과 x
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            price = int(input(search_price_message))
            # 오차 범위는 ±50%로 설정
            # 오차범위 ±50%인 가격목록에서 가격을 하나씩 뽑아 result_index에 인덱스번호 저장
            min = price * 0.5
            max = price * 1.5
            result_index = [price_list.index(i) for i in [price for price in price_list if min <= price <= max]]
            # price_list에서 값을 가져와 if min <= price <= max에 해당한 값들을 price에 담음
            # price 결과가 검색된 가격들을 i에 담고 price_list.index로 몇번째 방에 있는지 연산

            if len(result_index) != 0:          # result_index의 길이가 0이 아니면
                for i in result_index:          # 해당 인덱스에 해당되는 상품명과 가격을 모두 출력
                    print(f'{name_list[i]}, {price_list[i]}')
                    continue

            else:
                result_message = search_error_message   # result_index가 0이면 에러메시지 출력
    # 목록
    elif choice == 5:
        if len(name_list) == 0:         # (상품목록)name_list의 목록이 0인 경우
            result_message = no_item_message    # result_message 목록이 없다는 메시지 출력
        else:                                   # 상품목록이 있는 경우
            for i in range(len(name_list)):     # name_list의 길이를 i만큼 반복
                print(f'{name_list[i]}, {price_list[i]}')     # 반복문으로 상품목록의 개수만큼 반복, 상품목록(상품명, 가격) 출력
                continue

    # 나가기
    elif choice == 6:       #6번을 선택하면
        break               # 종료

    # 그 외
    else:
        result_message = error_message #그외의 에러는 다시 입력해주세요 => 에러 메시지

    print(result_message) # 결과값 출력
    result_message = ""


# find는 못찾으면 알려주지만 오류가 나지않음
# index는 못찾으면 오류 발생



