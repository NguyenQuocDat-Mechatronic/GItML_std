import pandas as pd
import numpy as np
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
        print('mới đọc xong')
    else:
        print("Sorry, I can't find this filename")
        return False
    return data
def analysis(data):
    print("**** ANALYZING ****")
    print('Total line of data: ',data.shape[0])
    # # dropping null value columns to avoid errors
    data.dropna(inplace=True)
    validLine = 0
    inValidLine = 0
    listResult = list()
    listWrongName = list()
    for i in range(data.shape[0]):
        k = data.iloc[i]
        k = k.values.tolist()
        print(k)
        for j in k:
            jSplit = j.split(',')
            for i in range(1,len(jSplit[0])):
                if ord(jSplit[0][i]) < 48 or ord(jSplit[0][i]) > 57:
                    listWrongName.append(j)
                    inValidLine += 1
            if len(jSplit[0])>1 and len(jSplit[0]) !=9:
                listWrongName.append(j)
                inValidLine +=1
            else:
                '''k la list ['aaa','1','2']'''
                for j in k:
                    counT = 0
                    for o in j:
                        if o == ',':
                            counT +=1
                    if counT == 25:
                        validLine +=1
                    else:
                        inValidLine +=1
                        listResult.append(j)
    print('Total valid lines of data: ',validLine)
    print('Total invalid lines of data:',inValidLine)
    for i in listResult:
        print('Invalid line of data: does not contain exactly 26 values:')
        print(i)
    for i in listWrongName:
        print('Invalid line of data: N# is invalid:')
        print(i)
    # # new = data["Name"]
    # # new = data["Name"].str.split(",", expand=True)
    # name = list(map(str, (range(0, new.shape[1] - 1))))
    # name.insert(0, 'Name')
    # # change title name from new data frame
    # data[name] = new
    # # print('data\n',data)
    # # data.to_csv('class.csv')
    # # Can I set the index column when reading a CSV using Python dask?
    # # data_csv = pd.read_csv('class.csv', index_col=0)
    # # print('origin',data_csv)
    # # print('dropNaN',data_csv.dropna())
    #
    # # data_csv.drop('0',1)
    # print(data)
    # print("**** ANALYZING ****")
    # print('Total line of data: ',data.shape[0])
    # validLine = 0
    # inValidLine = 0

    # for i in range(data.shape[0]):
    #     # print(data_csv.iloc[i][1:data_csv.shape[1]])
    #     # data_new = data_csv.iloc[i][0:data_csv.shape[1]]
    #
    #     data_new = data.iloc[i][0:26]
    #     print(data_new.shape)
    #     # dataAfterDrop = pd.DataFrame(data_new)
    #     """function dropna giúp loại bỏ nan"""
    #     # dataAfterDrop =dataAfterDrop.dropna()
    #     Name = data_new[0]
    #     if len(Name) != 9:
    #         rsNameWrong = data_new.values.tolist()
    #         listWrongName.append(rsNameWrong)
    #         print(rsNameWrong)
    #         inValidLine += 1
    #     elif data_new.shape[0] == 26:
    #         validLine +=1
    #     else:
    #         inValidLine +=1
    #         # k = dataAfterDrop.iloc[:]
    #         # k = data_new
    #         # print(k)
    #         rs = data_new.values.tolist()
    #         # print(rs)
    #         listResult.append(rs)

    # print(listResult)
    # for i in listResult:
    #     print('Invalid line of data: does not contain exactly 26 values:')
    #     strResult = str()
    #     for k in i[0:]:
    #         if pd.notna(k) :
    #             strResult += str(k) +','
    #         else:
    #             strResult += ''+','
    #     print(strResult)

# data = readFile()
# # dropping null value columns to avoid errors
# data.dropna(inplace = True)
# new data frame with split value columns








