import pandas as pd
iphone_df = pd.read_csv('../data/iphone.csv', index_col=0)
# print(iphone_df)

# 기본 값
# print(iphone_df.loc['iPhone 8', '메모리']) # 2GB

# 메모리 정보를 변경
iphone_df.loc['iPhone 8', '메모리'] = '2.5GB'
# print(iphone_df)

# 아이폰 출시 버전 변경
iphone_df.loc['iPhone 8', '출시 버전'] = 'iOS 10.3'
# print(iphone_df.loc['iPhone 8'])

# 한 줄을 통채로 변경할 때
# print(iphone_df.loc['iPhone 8'])
iphone_df.loc['iPhone 8'] = ['2016-09-22', 4.7, '2GB', 'iOS 11.0', 'No']
# print(iphone_df)

# 컬럼 한 줄 값 바꾸기
# print(iphone_df['디스플레이'])
iphone_df['디스플레이'] = ['4.7 in', '5.5 in', '6.5 in', '7.5 in', '8.0 in', '9.5 in', '10.7 in']
# print(iphone_df)

# Face ID 컬럼을 모두 No로 바꾸기
iphone_df['Face ID'] = ['No', 'No', 'No', 'No', 'No', 'No', 'No']
# print(iphone_df)

# 모든값을 똑같이 바꿀때
iphone_df['Face ID'] = 'Yes'
print(iphone_df)