import pandas as pd
import numpy as np
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# df = pd.read_csv(r'.\Data Files\class1.txt')


# add title to colum with (names=['Name'])
# data = pd.read_csv(r'.\data-files\Data Files\class1.txt',sep=" ", header=None,names=['Name'])


import mainFunction2
def menu():
    data,filename = mainFunction2.readFile()[0:2]
    while data is False:
        data = mainFunction2.readFile()
    mainFunction2.analysis(data)
    pointArray,csv = mainFunction2.cal()[0:2]
    mainFunction2.save(pointArray,csv,filename)
if __name__ == '__main__':
    menu()