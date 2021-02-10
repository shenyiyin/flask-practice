#data create

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
path=r'/data/'

n=100

weathers=['sunny','rainy','cloudy']
date=np.arange(1,n,1)
w=[]
t=[]
dict_init={}

for each in date:
    r1=random.randint(0,2)
    w.append(weathers[r1])
dict_init['date']=date
dict_init['weathers']=w



class  dataframe(object):
    def __init__(self):
        self.data=pd.DataFrame(dict_init)
        #data[]=....为加一列数据
        #df = pd.DataFrame(columns=('a', 'b', 'c'))
        #df = df.append([{'a': 10.0, 'b': 'name', 'c': 10}], ignore_index=True)加一行数据

    def data_append(self):
        dict_append=[]
        for each in self.data['weathers']:
            if each=='sunny':
                dict_append.append(20+random.randint(-3,3))
            if each =='rainy':
                dict_append.append(10+random.randint(-3,3))
            if each=='cloudy':
                dict_append.append(15+random.randint(-1,1))
        self.data['temperatures']=dict_append

    def plot(self):
        f=plt.figure()
        plt.plot(self.data["date"],self.data['temperatures'])
        plt.pause(1)


frame=dataframe()
frame.data_append()
print(frame.data)
frame.plot()
