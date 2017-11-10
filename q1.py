# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 23:32:24 2017
@author: Dell
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

data=pd.read_csv('FullData.csv')


k=data.groupby('Nationality')
#xTicks=k['Nationality']
#print(xTicks)
#xTicks=k['Nationality']
#print(k)
xTicks=['manish']
h=['0']
del h[0]
del xTicks[0]
i=0
for name,group in k:
    xTicks.insert(i,name)
    g=[group['Freekick_Accuracy'].agg(np.mean),group['Volleys'].agg(np.mean),group['Curve'].agg(np.mean),group['Long_Shots'].agg(np.mean),
       group['Finishing'].agg(np.mean),group['Shot_Power'].agg(np.mean),group['Ball_Control'].agg(np.mean),group['Marking'].agg(np.mean),
       group['Attacking_Position'].agg(np.mean),group['Vision'].agg(np.mean),group['Acceleration'].agg(np.mean),group['Strength'].agg(np.mean),
       group['Balance'].agg(np.mean),group['Agility'].agg(np.mean),group['Heading'].agg(np.mean)]
    h.insert(i,np.mean(g))
    i=i+1



#print(h)
 #grouped['Points'].agg([np.sum, np.mean, np.std])
#3ws=k.('Freekick_Accuracy' , 'Volleys' , 'Curve' , 'Long_Shots' , 'Finishing' , 'Shot_Power' , 'Ball_Control' , 'Marking' ,
#	           'Attacking_Position' , 'Vision' , 'Acceleration' , 'Strength' , 'Balance' , 'Agility' , 'Heading')


x = list(range(160))
pl.xticks(x, xTicks)
pl.xticks(range(160), xTicks,rotation=45) #writes strings with 45 degree angle
pl.title('best goal')
pl.xlabel('Teams')
pl.ylabel('Attributes')
pl.plot(x,h,'*',color='red')
pl.show()
