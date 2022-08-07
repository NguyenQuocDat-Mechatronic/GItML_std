import pandas as pd
import numpy as np

"""ReadFile function : readfile from input. outpunt: data is read, name of file"""
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
    return data,fileName

"""Analysis Function : analyze data check whether flow rule. Output vaild.csv"""
def analysis(data):
    print("**** ANALYZING ****")
    print('Total line of data: ',data.shape[0])
    # # dropping null value columns to avoid errors
    data.dropna(inplace=True)
    validLine = 0
    inValidLine = 0
    listResult = list()
    listWrongName = list()
    listValid = list()
    for i in range(data.shape[0]):
        k = data.iloc[i]
        k = k.values.tolist()
        # k is list of each row
        for j in k:
            jSplit = j.split(',')
            for i in range(1,len(jSplit[0])):
                # check number or not
                if ord(jSplit[0][i]) < 48 or ord(jSplit[0][i]) > 57:
                    listWrongName.append(j)
                    inValidLine += 1
            if len(jSplit[0])>1 and len(jSplit[0]) !=9:
                listWrongName.append(j)
                inValidLine +=1
            else:
                for j in k:
                    counT = 0
                    for o in j:
                        if o == ',':
                            counT +=1
                    if counT == 25:
                        validLine +=1
                        listValid.append(j)
                    else:
                        inValidLine +=1
                        listResult.append(j)
    if inValidLine == 0:
        print('No errors found!')
    else:
        for i in listResult:
            print('Invalid line of data: does not contain exactly 26 values:')
            print(i)
        for i in listWrongName:
            print('Invalid line of data: N# is invalid:')
            print(i)
    print("**** REPORT ****")
    print('Total valid lines of data: ', validLine)
    print('Total invalid lines of data:', inValidLine)
    csvValid = pd.DataFrame(listValid)
    # Important : index = False không tự tạo thêm index.
    csvValid.to_csv('valid.csv',mode='w', index=False)

"""Cal function : calculte point by Name, output : point array, new : array """
def cal():
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    lstAnswer = answer_key.split(",")
    # add colum name
    dataCsv = pd.read_csv('valid.csv', sep=" ", names=['Name'])
    # split name colum
    new = dataCsv["Name"].str.split(",", expand=True)
    new = pd.DataFrame(new[1:])
    # create empty array
    pointArray = np.empty([0,25],dtype = int)
    # duyệt từng row
    for i in range (0,new.shape[0]):
        listVal = new.iloc[i]
        k = 0
        point = 0
        # compare each value
        for rs in listVal[1:]:
            if rs == "":
                pass
            elif rs == lstAnswer[k]:
                point +=4
            else:
                point -=1
            k +=1
        pointArray = np.append(pointArray,point)
    print('Mean (average) score: ',round(np.average(pointArray),2))
    print('Highest score: ',round(np.max(pointArray),2))
    print('Lowest score: ', round(np.min(pointArray), 2))
    print('Range of scores: ',round(np.max(pointArray)-np.min(pointArray),2))
    print('Median score: ',round(np.median(pointArray)))
    return pointArray,new

"""save function : save file to file.txt, input : point, scvValid , file name input"""
def save(pointArrary,csvValid,filename):
    strFile = str(filename) +'_grades.txt'
    with open(strFile,mode='w') as writeFile:
        for i in range(0,csvValid.shape[0]):
            strWrite = str(csvValid[0][i+1])+","+str(pointArrary[i]) +"\n"
            writeFile.write(strWrite)



