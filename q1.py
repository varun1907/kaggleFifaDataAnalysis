import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import math

data=pd.read_csv('FullData.csv')

k=data.groupby('Nationality')

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

x = list(range(160))
pl.xticks(x, xTicks)
pl.xticks(range(160), xTicks,rotation=45)
pl.title('best goal')
pl.xlabel('Teams')
pl.ylabel('Attributes')
pl.plot(x,h,'*',color='red')
pl.show()


#question first finishes


#question second

i=0;
m=['0']
del m[0]
for key,value in k:
	aggression=[value['Aggression'].agg(np.mean)]
	m.insert(i,aggression)
	i+=1

pl.xticks(x, xTicks)
pl.xticks(range(160), xTicks,rotation=45)
pl.title('Aggression')
pl.xlabel('Teams')
pl.ylabel('Attributes')
pl.plot(x,m,'*',color='blue')
pl.show()


#question second finishes







#question fifth
#ax = plt.subplots()
dat=pd.read_csv('FullData1.csv')
clubJoining=dat['Club_Joining'].tolist()
contractExpiry=dat['Contract_Expiry'].tolist()
joiningYear=['1']
del joiningYear[0]

#print(contractExpiry.isnull().values.any())



i=0
dat=pd.read_csv('FullData1.csv')
name = dat['Name'].tolist()

clubJoining=dat['Club_Joining'].tolist()
contractExpiry=dat['Contract_Expiry'].tolist()
joiningYear=['1']
del joiningYear[0]
s=['a']
del s[0]
while i<100:
    c=clubJoining[i]
    c=c[-4:]
    joiningYear.insert(i,c);
    joiningYear[i]=float(joiningYear[i])
    joiningYear[i]=contractExpiry[i]-joiningYear[i]
    s.insert(i,name[i])
    i=i+1


rg=list(range(100))
pl.xticks(rg, s)
pl.xticks(range(100), s,rotation=90)
pl.title('Contract Period')
pl.xlabel('Player')
pl.ylabel('Duration')
pl.plot(rg,joiningYear,'*',color='blue')
plt.grid()
pl.show()
