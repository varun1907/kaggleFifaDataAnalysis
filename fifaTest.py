import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('FullData.csv')

name=data['Name'];



ws=data.loc[:,('Freekick_Accuracy' , 'Volleys' , 'Curve' , 'Long_Shots' , 'Finishing' , 'Shot_Power' , 'Ball_Control' , 'Marking' ,
	           'Attacking_Position' , 'Vision' , 'Acceleration' , 'Strength' , 'Balance' , 'Agility' , 'Heading')]


a=ws.mean(axis=1);

b=a.tolist()
nme =name.tolist()
plt.plot(nme,b);
plt.show()