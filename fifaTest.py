# -*- coding: utf-8 -*-
'''

Created on Thu Nov  9 23:32:
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

data=pd.read_csv('FullData.csv')

xTicks=data['Name'];

ws=data.loc[:,('Freekick_Accuracy' , 'Volleys' , 'Curve' , 'Long_Shots' , 'Finishing' , 'Shot_Power' , 'Ball_Control' , 'Marking' ,
	           'Attacking_Position' , 'Vision' , 'Acceleration' , 'Strength' , 'Balance' , 'Agility' , 'Heading')]

y=ws.mean(axis=1);
x = list(range(17588))
pl.xticks(x, xTicks)
pl.xticks(range(2), xTicks, rotation=45) #writes strings with 45 degree angle
pl.title('best goal')
pl.xlabel('players')
pl.ylabel('total goals')
pl.plot(x,y)
pl.show()
