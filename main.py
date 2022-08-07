import pandas as pd
import numpy as np

import mainFunction2
def menu():
    try:
        data,filename = mainFunction2.readFile()[0:2]
    except:
        data = mainFunction2.readFile()
    mainFunction2.analysis(data)
    pointArray,csv = mainFunction2.cal()[0:2]
    mainFunction2.save(pointArray,csv,filename)
if __name__ == '__main__':
    menu()