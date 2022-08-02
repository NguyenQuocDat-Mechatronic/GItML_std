import pandas as pd
import numpy as np
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# df = pd.read_csv(r'.\Data Files\class1.txt')


# add title to colum with (names=['Name'])
# data = pd.read_csv(r'.\data-files\Data Files\class1.txt',sep=" ", header=None,names=['Name'])

def readFile():
    print("Enter a filename:")
    fileName = input()
    if fileName in ["class1", "class2", "class3", "class4", "class5", "class6", "class7" ,"class8"]:
        print(f'Successfully opened {fileName}.txt')
        strName = fileName+'.txt'
        data  = pd.read_csv(strName,sep=" ",names=['Name'])
    else:
        print("Sorry, I can't find this filename")
        return False
    return data
def analysis(data):
    # # dropping null value columns to avoid errors
    data.dropna(inplace=True)
    new = data["Name"].str.split(",", expand=True)
    name = list(map(str, (range(0, new.shape[1] - 1))))
    name.insert(0, 'Name')
    # change title name from new data frame
    data[name] = new
    # print('data\n',data)
    print('first',data)
    data.to_csv('class.csv')
    # Can I set the index column when reading a CSV using Python dask?
    data_csv = pd.read_csv('class.csv', index_col=0)
    # print('origin',data_csv)
    # print('dropNaN',data_csv.dropna())

    # data_csv.drop('0',1)
    print(data_csv)
    print("**** ANALYZING ****")
    print('Total line of data: ',data_csv.shape[0])
    validLine = 0
    inValidLine = 0
    listResult = list()
    listWrongName = list()
    for i in range(data_csv.shape[0]):
        # print(data_csv.iloc[i][1:data_csv.shape[1]])
        # data_new = data_csv.iloc[i][0:data_csv.shape[1]]
        data_new = data_csv.iloc[i]
        print(data_new.shape)
        # dataAfterDrop = pd.DataFrame(data_new)
        """function dropna giúp loại bỏ nan"""
        # dataAfterDrop =dataAfterDrop.dropna()
        Name = data_new[0]
        if len(Name) != 9:
            rsNameWrong = data_new.values.tolist()
            listWrongName.append(rsNameWrong)
            print(rsNameWrong)
            inValidLine += 1
        elif data_new.shape[0] == 26:
            validLine +=1
        else:
            inValidLine +=1
            # k = dataAfterDrop.iloc[:]
            # k = data_new
            # print(k)
            rs = data_new.values.tolist()
            # print(rs)
            listResult.append(rs)
    print('Total valid lines of data: ',validLine)
    print('Total invalid lines of data:',inValidLine)
    print(listResult)
    for i in listResult:
        print('Invalid line of data: does not contain exactly 26 values:')
        strResult = str()
        for k in i[0:]:
            if pd.notna(k) :
                strResult += str(k) +','
            else:
                strResult += ''+','
        print(strResult)

# data = readFile()
# # dropping null value columns to avoid errors
# data.dropna(inplace = True)
# new data frame with split value columns








