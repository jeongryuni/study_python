import pandas as pd
iphone_df = pd.read_csv('../data/iphone.csv', index_col=0)

# 여러줄을 한번에 값을 변경하기
# print(iphone_df[['디스플레이', 'Face ID']]) # 디스플레이와 Face ID만 출력하기
iphone_df[['디스플레이', 'Face ID']] = 'x'
# print(iphone_df)
'''
                      출시일 디스플레이  메모리     출시 버전 Face ID
iPhone 7       2016-09-16     x  2GB  iOS 10.0       x
iPhone 7 Plus  2016-09-16     x  3GB  iOS 10.0       x
iPhone 8       2017-09-22     x  2GB  iOS 11.0       x
iPhone 8 Plus  2017-09-22     x  3GB  iOS 11.0       x
iPhone X       2017-11-03     x  3GB  iOS 11.1       x
iPhone XS      2018-09-21     x  4GB  iOS 12.0       x
iPhone XS Max  2018-09-21     x  4GB  iOS 12.0       x
'''

# iPhone 7과 X만 o로 바꾸기
# print(iphone_df.loc[['iPhone 7', 'iPhone X']])
iphone_df.loc[['iPhone 7', 'iPhone X']] = 'o'
print(iphone_df)