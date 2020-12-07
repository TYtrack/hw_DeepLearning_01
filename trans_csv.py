import csv
import numpy as np
import pandas as pd


with open("train_feature.csv",encoding="big5") as f1:
    last_csv=[]
    target=[]
    data=np.loadtxt(f1,str,delimiter=",")


    for i in data[1:]:
        temp=[]
        for index,j in enumerate(i):
            if index==11:
                target.append(j)
                continue
            if index==0:
                continue
            if j=="NR":
                j=0
                temp.append(0)
            elif "/" not in j:
                try:
                    temp.append(float(j))
                except:
                    print("&",j)
        last_csv.append(temp)
    print(last_csv[:10])

    pd.DataFrame(target).to_csv("last_train_target.csv")
    pd.DataFrame(last_csv).to_csv("last_train_feature.csv")


with open("test_feature.csv",encoding="big5") as f2:
    last_csv=[]
    data=np.loadtxt(f2,str,delimiter=",")


    for i in data[1:]:
        temp=[]
        for index,j in enumerate(i):
            if  index==0:
                continue
            if j=="NR":
                j=0
                temp.append(0)
            elif "id" not in j:
                try:
                    temp.append(float(j))
                except:
                    print("&",j)
        last_csv.append(temp)
    print(last_csv[:10])
    pd.DataFrame(last_csv).to_csv("last_test_feature.csv")
