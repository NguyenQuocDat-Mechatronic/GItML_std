import pandas as pd
import numpy as np
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# df = pd.read_csv(r'.\Data Files\class1.txt')


# add title to colum with (names=['Name'])
# data = pd.read_csv(r'.\data-files\Data Files\class1.txt',sep=" ", header=None,names=['Name'])

import mainFunction
import mainFunction2
def menu():
    data = mainFunction2.readFile()
    while data is False:
        data = mainFunction2.readFile()
    mainFunction2.analysis(data)

if __name__ == '__main__':
    menu()