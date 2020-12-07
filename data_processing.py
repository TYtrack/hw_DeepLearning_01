import csv
import numpy as np
import pandas as pd

with open("ml2020spring-hw1/train.csv",encoding="big5") as f1:
    a=np.loadtxt(f1,str,delimiter=",")
    print(a[:10])
    print(a.shape)
    #a=np.array(240,18,head="")
    count=0
    dict_a={}
    list_dict=[]
    for i in a[1:]:
        dict_a[i[2]]=i[11]
        count += 1
        if count == 10:
            dict_a["PM2.5_10"] = i[12]


        if count==18:
            dict_a["date"]=i[0]
            list_dict.append(dict_a)
            dict_a={}
            count=0
    pd.DataFrame(list_dict).to_csv("train_feature.csv")
    print(list_dict[:5])


with open("ml2020spring-hw1/test.csv",encoding="big5") as f2:
    b=np.loadtxt(f2,str,delimiter=",")
    print(b[:10])
    count = 0
    dict_b = {}
    list_dict_b = []
    for i in b[0:]:
        dict_b[i[1]] = i[10]
        count += 1

        if count == 18:
            dict_b["date"] = i[0]
            list_dict_b.append(dict_b)
            dict_b = {}
            count = 0
    pd.DataFrame(list_dict_b).to_csv("test_feature.csv")
    print(list_dict_b[:5])
    #print(b[:5])
    #print(b.shape)

with open("ml2020spring-hw1/sample_submission.csv",encoding="big5") as f3:
    c =np.loadtxt(f3,str,delimiter=",")
    #print(c[:5])
    #print(c.shape)