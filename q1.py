import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import math
import operator


data=pd.read_csv('FullData.csv')

k=data.groupby('Nationality')
xTicks=['varun']
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
plt.grid()
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
plt.grid()
pl.show()


#question second finishes



#question third

africa = ['Algeria','Guinea Bissau','São Tomé & Príncipe','Guinea Bissau ','DR Congo','Central African Rep.','Angola','Benin','Botswana',
              'Burkina Faso','Burundi','Cameroon','Cape Verde','Central African Republic','Chad','Comoros','Congo','Congo Democratic Republic of',
              'Djibouti','Egypt','Equatorial Guinea','Eritrea','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea-Bissau','Ivory Coast','Kenya',
              'Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria',
              'Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Swaziland',
              'Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe','Burkina Faso']
asia = ['Afghanistan','China PR','Korea Republic','Palestine','Korea DPR','Timor-Leste','Chinese Taipei','Bahrain','Armenia','Bangladesh',
            'Azerbaijan','Bhutan','Brunei','Burma (Myanmar)','Cambodia','China','East Timor','India','Indonesia','Iran','Iraq','Israel','Japan',
            'Jordan','Georgia','Kazakhstan','North Korea','South Korea','Kuwait','Kyrgyzstan','Laos','Lebanon','Malaysia','Maldives','Mongolia',
            'Nepal','Oman','Pakistan','Philippines','Qatar','Russian Federation','Saudi Arabia','Singapore','Sri Lanka','Syria','Tajikistan',
            'Thailand','Turkey','Turkmenistan','United Arab Emirates','Uzbekistan','Vietnam','Yemen']
europe =  ['Albania','FYR Macedonia','Faroe Islands','Serbia','Gibraltar','Kosovo','Bosnia Herzegovina','Andorra','Scotland','Austria','Belarus',
              'Belgium','Bosnia and Herzegovina','Bulgaria','Croatia','Cyprus','Czech Republic','Denmark','Estonia','Finland','France','Germany',
              'Greece','Hungary','Iceland','Republic of Ireland','Italy','Latvia','Liechtenstein','Northern Ireland','Lithuania','Luxembourg',
              'Macedonia','Malta','Moldova','Monaco','Montenegro','Netherlands','Norway','Poland','Portugal','Romania','Russia','San Marino','Serbi',
              'Slovakia','Slovenia','Spain','Sweden','Switzerland','Ukraine','England','Vatican City','Republic of Ireland','Wales']
north_america = ['Antigua and Barbuda','Puerto Rico','St Lucia','Antigua & Barbuda','Montserrat','Bermuda','St Kitts Nevis','Bahamas','Barbados',
                 'Belize','Canada','Costa Rica','Cuba','Dominica','Dominican Republic','El Salvador','Grenada','Guatemala','Haiti','Honduras',
                 'Jamaica','Mexico','Nicaragua','Panama','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Trinidad and Tobago',
                 'United States']
australia = ['Australia','FIFA16_NationName_215','Guam','Fiji','Kiribati','Marshall Islands','Micronesia','Nauru','New Zealand','Palau',
             'Papua New Guinea','Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu']
south_america =['Argentina','Curacao','Trinidad & Tobago','Aruba','Bolivia','Brazil','Chile','Colombia','Ecuador','Guyana','Paraguay','Peru',
                'Suriname','Uruguay','Venezuela']

nationality=data['Nationality'].tolist()
continent=[]
i=0
while i<17588:
    if nationality[i] in africa:
        continent.insert(i,'africa')
    elif nationality[i] in asia:
        continent.insert(i,'asia')
    elif nationality[i] in europe:
        continent.insert(i,'europe')
    elif nationality[i] in north_america:
        continent.insert(i,'north_america')
    elif nationality[i] in australia:
        continent.insert(i,'australia')
    elif nationality[i] in south_america:
        continent.insert(i,'south_america')
    i=i+1


se = pd.Series(continent)
data['Continent'] = se.values





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


#print(g)
sorted_d = sorted(g.items(), key=operator.itemgetter(1),reverse=True)
#print(sorted_d)



key1=[]
key1=[x[0] for x in sorted_d]
value1=[]
value1=[x[1] for x in sorted_d]
key2=[]
value2=[]
i=0
while i<5:
    key2.insert(i,key1[i])
    value2.insert(i,value1[i])
    i=i+1


plt.pie(value2, labels=key2,
                autopct='%1.1f%%', shadow=True, startangle=90)


plt.show()
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
