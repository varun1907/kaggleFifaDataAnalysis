import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import math
import operator

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






#question fourth


clubInput=input("Enter the club")
varun=data.set_index('Club')
gupta=varun.loc[clubInput]
#gupta=[varun['Reactions']agg(np.mean)]

g={'Ball_Control'       : gupta['Ball_Control'].agg(np.mean),
   'Dribbling'          : gupta['Dribbling'].agg(np.mean),
   'Marking'            : gupta['Marking'].agg(np.mean),
   'Sliding_Tackle'     : gupta['Sliding_Tackle'].agg(np.mean),
   'Standing_Tackle'    : gupta['Standing_Tackle'].agg(np.mean),
   'Aggression'         : gupta['Aggression'].agg(np.mean),
   'Reactions'          : gupta['Reactions'].agg(np.mean),
   'Attacking_Position' : gupta['Attacking_Position'].agg(np.mean),
   'Interceptions'      : gupta['Interceptions'].agg(np.mean),
   'Vision'             : gupta['Vision'].agg(np.mean),
   'Composure'          : gupta['Composure'].agg(np.mean),
   'Crossing'           : gupta['Crossing'].agg(np.mean),
   'Short_Pass'         : gupta['Short_Pass'].agg(np.mean),
   'Long_Pass'          : gupta['Long_Pass'].agg(np.mean),
   'Acceleration'       : gupta['Acceleration'].agg(np.mean),
   'Speed'              : gupta['Speed'].agg(np.mean),
   'Stamina'            : gupta['Stamina'].agg(np.mean),
   'Strength'           : gupta['Strength'].agg(np.mean),
   'Balance'            : gupta['Balance'].agg(np.mean),
   'Agility'            : gupta['Agility'].agg(np.mean),
   'Jumping'            : gupta['Jumping'].agg(np.mean),
   'Heading'            : gupta['Heading'].agg(np.mean),
   'Shot_Power'         : gupta['Shot_Power'].agg(np.mean),
   'Finishing'          : gupta['Finishing'].agg(np.mean),
   'Long_Shots'         : gupta['Long_Shots'].agg(np.mean),
   'Curve'              : gupta['Curve'].agg(np.mean),
   'Freekick_Accuracy'  : gupta['Freekick_Accuracy'].agg(np.mean),
   'Penalties'          : gupta['Penalties'].agg(np.mean),
   'Volleys'            : gupta['Volleys'].agg(np.mean)}

sorted_d = sorted(g.items(), key=operator.itemgetter(1),reverse=True)
print(sorted_d)









#question fifth


#ax = plt.subplots()
i=0
name = data['Name'].tolist()

clubJoining=data['Club_Joining'].tolist()
contractExpiry=data['Contract_Expiry'].tolist()
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
