import pandas as pd
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# df = pd.read_csv(r'.\Data Files\class1.txt')
name = list(map(str,(range(0,25))))
name.insert(0,'Name')
data = pd.read_csv(r'.\data-files\Data Files\class1.txt',sep=" ", header=None,names=['Name'])
# dropping null value columns to avoid errors
data.dropna(inplace = True)
# new data frame with split value columns
new= data["Name"].str.split(",", expand = True)

# making separate first name column from new data frame ( chọn tên first name cho từng cột)
# data["First Name"] = new[0]

# making separate last name column from new data frame ( chọn tên last name cho cột số 2)
# data["Last Name"] = new[1]
# change title name from new data frame
data[name] = new
data.to_csv('class1.csv')
# Can I set the index column when reading a CSV using Python dask?
data_csv = pd.read_csv('class1.csv',index_col=0)
# data_csv.drop('0',1)
print(data_csv)
# index_name=df.index.name
# df.index.name='Index1'
# df_index = pd.DataFrame(df)
# df = pd.DataFrame(df,index='Name')
# df_name  = df['name'].str.split()
# df.to_csv('test.csv')
# # df_name = df.iloc[0]
# df_split = df['Name'].str.split(pat = ',',expand = True)
#
# df[[name]] = df_split
# df_split.to_csv('test.csv')
# print(df_split.head(21))
# # print('----')
# # print(df.head(21))
# print(df_split.shape)